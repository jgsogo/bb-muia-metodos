# !/usr/bin/env python
# -*- coding: utf-8 -*-


import random
from muia.distribution.base import Distribution


class ClientManager(object):
    _arrival_distribution = None
    _demand_distribution = None

    def __init__(self, random_engine):
        assert isinstance(random_engine, random.Random), "'random_engine' not a random.Random instance"
        self._engine = random_engine

    def set_arrival(self, distribution_class, **kwargs):
        assert issubclass(distribution_class, Distribution), "Not a distribution"
        self._arrival_distribution = distribution_class(self._engine, **kwargs)

    def set_demand(self, distribution_class, **kwargs):
        assert issubclass(distribution_class, Distribution), "Not a distribution"
        self._demand_distribution = distribution_class(self._engine, **kwargs)

    def next_hour(self):
        # Returns (n_clients, (client_1, client_2, ...)) tuple
        n_clients = self._arrival_distribution.random()
        request = []
        for i in xrange(n_clients):
            request.append(self._demand_distribution.random())
        return n_clients, request

