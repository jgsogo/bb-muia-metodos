# !/usr/bin/env python
# -*- coding: utf-8 -*-

class Store(object):
    _cost_per_unit = 0.0001 # Coste de almacenamiento por unidad de producto y unidad de tiempo
                            # TODO: ¿Cuál es la unidad de tiempo? En otras partes se habla de horas...

    def __init__(self, initial_stock, on_stock_change=None):
        self._initial_stock = initial_stock
        self._stock = self._initial_stock
        self._on_stock_change = on_stock_change

    def reset(self):
        self._stock = self._initial_stock

    def set_on_stock_change(self, on_stock_change):
        self._on_stock_change = on_stock_change

    def set_cost_per_unit(self, cost_per_unit):
        # Coste de almacenamiento por unidad de producto
        self._cost_per_unit = cost_per_unit

    def get_stock(self):
        return self._stock

    def put_items(self, quantity):
        self._stock += quantity

    def grab_items(self, quantity):
        q = min(quantity, self._stock)
        self._stock = self._stock - q
        if self._on_stock_change:
            self._on_stock_change(self._stock)
        return q

