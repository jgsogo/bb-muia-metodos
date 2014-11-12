# !/usr/bin/env python
# -*- coding: utf-8 -*-


import random
from muia.distribution.base import Distribution
from muia.distribution.poisson_variate import PoissonVariate
from muia.distribution.exponential_variate import ExponentialVariate


class ClientManager(object):
    _arrival_distribution = None
    _demand_distribution = None

    def __init__(self, random_engine):
        assert isinstance(random_engine, random.Random), "'random_engine' not a random.Random instance"
        self._engine = random_engine

    def set_arrival(self, distribution_class, **kwargs):
        assert issubclass(distribution_class, PoissonVariate), "Poisson distribution expected"
        self._arrival_poisson = distribution_class(random_engine=self._engine, **kwargs)
        self._arrival_exp = ExponentialVariate(lambd=self._arrival_poisson._L, random_engine=self._engine)

    def set_demand(self, distribution_class, **kwargs):
        assert issubclass(distribution_class, Distribution), "Not a distribution"
        self._demand_distribution = distribution_class(random_engine=self._engine, **kwargs)

    def next_hour(self):
        # Returns (n_clients, (client_1, client_2, ...)) tuple
        #   - number of clients within next hour
        #   - number of articles requested by each client
        n_clients = self._arrival_poisson.random()
        request = []
        for i in xrange(n_clients):
            request.append(self._demand_distribution.random())
        return n_clients, request

    def get_next(self):
        # Return time_to_next, items_requested
        #   - time to next client
        #   - articles requested by next client
        t = self._arrival_exp.random()
        r = self._demand_distribution.random()
        return t, r