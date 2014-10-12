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


def test():
    print("Exponential Variate")

    import random
    lambd = 1.0
    generator = ExponentialVariate(lambd, random.Random())

    n = 10
    print(" - generate %r random number from Exp(%r)" % (n, lambd))
    i = 0
    while i<n:
        print("\t\t %r" % generator.random())
        i +=1

if __name__ == "__main__":
    test()