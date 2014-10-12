# !/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import Distribution

class DiscreteVariate(Distribution):

    def __init__(self, prob_list, random_engine):
        super(Distribution, self).__init__(random_engine)
        assert sum(prob_map.keys()) == 1, "Probabilities must sum 1"
        self._prob_map = prob_map # TODO: Reordenador de mayor probabilidad a menor

    def random(self):
        p = self._engine.random()

        #TODO: Implementar
