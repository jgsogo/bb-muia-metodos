# !/usr/bin/env python
# -*- coding: utf-8 -*-

from math import exp
from .base import Distribution

class PoissonVariate(Distribution):
    _P = None
    _F = None

    def __init__(self, lambd, random_engine):
        super(PoissonVariate, self).__init__(random_engine)
        self._lambd = lambd
        self._P = exp(-self._lambd)
        self._F = self._P

    def random(self):
        u = self._engine.random()
        k = 0
        while u > self._F:
            k += 1
            self._P *= self._lambd/k
            self._F += self._P
        return k

def test():
    print("Poisson Distribution")

    import random
    lambd = 0.5
    generator = PoissonVariate(lambd, random.Random())

    n = 10
    print(" - generate %r random number from Poisson(%r)" % (n, lambd))
    i = 0
    while i<n:
        print("\t\t %r" % generator.random())
        i +=1

if __name__ == "__main__":
    test()