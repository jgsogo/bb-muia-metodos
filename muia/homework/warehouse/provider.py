# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import math
from muia.distribution.base import Distribution

class Provider(object):
    _fix_cost = 10.
    _unit_price = 1.
    _offers = {}
    _order_time_distribution = None

    def __init__(self, random_engine):
        assert isinstance(random_engine, random.Random), "'random_engine' not a random.Random instance"
        self._engine = random_engine

    def set_order_time(self, distribution_class, **kwargs):
        assert issubclass(distribution_class, Distribution), "Not a distribution"
        self._order_time_distribution = distribution_class(random_engine=self._engine, **kwargs)

    def set_unit_cost(self, fix_cost, unit_price):
        # Coste por unidad de producto y coste fijo por cada pedido
        self._fix_cost = fix_cost
        self._unit_price = unit_price

    def set_offer(self, quatity_gte, unit_price):
        # Ofertas: coste unitario por cantidad
        self._offers[quatity_gte] = unit_price

    def get_unit_price(self, quantity):
        unit_price = self._unit_price
        # Comprobar si existe alguna oferta para esta cantidad
        for key, value in self._offers.iteritems():
            if key <= quantity:
                unit_price = value
                break
        return unit_price

    def get_order_price(self, quantity):
        return self._fix_cost + self.get_unit_price(quantity)*quantity

    def get_order_time(self):
        return self._order_time_distribution.random()

    def get_order(self, quantity):
        price = self.get_order_price(quantity)
        t = self.get_order_time()
        return price, quantity, t
