# !/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import Distribution

class NormalVariate(Distribution):

    def __init__(self, mu, sigma, random_engine):
        super(NormalVariate, self).__init__(random_engine)
        self._mu = mu
        self._sigma = sigma

    def random(self):
        # TODO: Implementar el nuestro propio
        return self._engine.normalvariate(self._mu, self._sigma)
