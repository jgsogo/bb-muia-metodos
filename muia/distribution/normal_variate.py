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


def test():
    print("Normal Variate")

    import random
    mu = 0.0
    sigma = 1.0
    generator = NormalVariate(mu, sigma, random.Random())

    n = 10
    print(" - generate %r random number from N(%r, %r)" % (n, mu, sigma))
    i = 0
    while i<n:
        print("\t\t %r" % generator.random())
        i +=1

if __name__ == "__main__":
    test()