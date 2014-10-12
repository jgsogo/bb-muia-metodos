# !/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import Distribution

class DiscreteVariate(Distribution):

    def __init__(self, prob_list, random_engine):
        super(DiscreteVariate, self).__init__(random_engine)
        self._prob_list = prob_list
        # TODO: Comprobar que suman 1 las probabilidades
        # TODO: Ordenar probabilidades de mayor a menor

    def random(self):
        # TODO: Revisar
        u = self._engine.random()
        i = 0
        p = self._prob_list[0][0]
        while u > p:
            i += 1
            p += self._prob_list[i][0]
        return self._prob_list[i][1]


def test():
    print("Discrete Distribution")

    import random
    prob_list = [(0.1, 1), (0.3, 2), (0.4, 3), (0.2, 4)]
    generator = DiscreteVariate(prob_list, random.Random())

    n = 10
    print(" - generate %r random from Discrete(%r)" % (n, prob_list))
    i = 0
    while i<n:
        print("\t\t %r" % generator.random())
        i +=1

if __name__ == "__main__":
    test()