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

    n = 1000
    print(" - generate %r random number from N(%r, %r)" % (n, mu, sigma))
    data = [generator.random() for i in xrange(n)]
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        # TODO: Implement histogram with numpy and plot
    except ImportError:
        import math
        mean = sum(data)/n
        sd = math.sqrt(sum((x-mean)**2 for x in data)/n)
        print("   + mean: %s" % (mean))
        print("   + std dev: %s" % (sd))


if __name__ == "__main__":
    test()