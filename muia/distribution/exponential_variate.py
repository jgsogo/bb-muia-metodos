# !/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import Distribution

class ExponentialVariate(Distribution):

    def __init__(self, lambd, random_engine):
        super(ExponentialVariate, self).__init__(random_engine)
        self._lambd = lambd

    def random(self):
        # TODO: Implementar el nuestro propio
        return self._engine.expovariate(self._lambd)
