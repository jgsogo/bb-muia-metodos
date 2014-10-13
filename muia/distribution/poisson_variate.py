# !/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from .base import Distribution

class PoissonVariate(Distribution):
    _L = None

    def __init__(self, lambd, random_engine):
        super(PoissonVariate, self).__init__(random_engine)
        self._lambd = lambd
        self._L = math.exp(-self._lambd)

    def random(self):
        # \sa: http://en.wikipedia.org/wiki/Poisson_distribution
        # Donald E. Knuth (1969). Seminumerical Algorithms. The Art of Computer Programming, Volume 2. Addison Wesley.
        k = 1
        p = self._engine.random()
        while p > self._L:
            p = p * self._engine.random()
            k += 1
        return k - 1

def test():
    print("Poisson Distribution")

    import random
    lambd = 4
    generator = PoissonVariate(lambd, random.Random())

    n = 10
    print(" - generate %r random number from Poisson(%r)" % (n, lambd))
    i = 0
    while i<n:
        print("\t\t %r" % generator.random())
        i +=1

if __name__ == "__main__":
    test()