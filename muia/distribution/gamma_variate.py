# !/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt, log, pi, cos, sin
from .base import Distribution
from .exponential_variate import ExponentialVariate


class GammaVariate(Distribution):

    def __init__(self, alpha, beta, random_engine):
        super(GammaVariate, self).__init__(random_engine)
        self._alpha = alpha
        self._beta = beta
        self.exp = ExponentialVariate(lambd=1.0, random_engine=random_engine)

    def random(self):
        x = 0.0
        for i in xrange(0, self._alpha):
            x = x + self.exp.random()

        return x/float(self._beta)


def test():
    print("Gamma Variate")

    import random
    alpha = 3
    beta = 2
    generator = GammaVariate(alpha, beta, random.Random())

    n = 1000
    print(" - generate %r random number from G(%r, %r)" % (n, alpha, beta))
    data = [generator.random() for i in xrange(n)]
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        # TODO: Implement histogram with numpy and plot
    except ImportError:
        import math
        print "done!"

if __name__ == "__main__":
    test()