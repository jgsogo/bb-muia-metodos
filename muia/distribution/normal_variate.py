# !/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import Distribution

class NormalVariate(Distribution):

    def __init__(self, mu, sigma, engine_class, seed=None):
        super(NormalVariate, self).__init__(engine_class, seed)
        self._mu = mu
        self._sigma = sigma

    def random(self):
        # TODO: Implementar el nuestro propio
        return self._engine.normalvariate(self._mu, self._sigma)
