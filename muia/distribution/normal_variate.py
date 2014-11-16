# !/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt, log, pi, cos, sin
from .base import Distribution

class NormalVariate(Distribution):

    def __init__(self, mu, sigma, random_engine):
        super(NormalVariate, self).__init__(random_engine)
        self._mu = mu
        self._sigma = sigma

    def random(self):
        u1 = self._engine.random()
        u2 = self._engine.random()
        r = sqrt(-2*log(u1))
        t = 2*pi*u2
        x = self._mu + self._sigma*r*cos(t)
        y = self._mu + self._sigma*r*sin(t)
        return x

def test():
    print("Normal Variate")

    import random_impl
    mu = 48.0
    sigma = 0.8
    generator = NormalVariate(mu, sigma, random_impl.Random())

    n = 1000
    print(" - generate %r random_impl number from N(%r, %r)" % (n, mu, sigma))
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