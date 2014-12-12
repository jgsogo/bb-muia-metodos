# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random
import math
from muia.distribution.gamma_variate import GammaVariate
from muia.random_impl import MersenneTwisterEngine

def run():
    sys.stdout.write("="*13)
    sys.stdout.write("\n== Exercise 3\n")
    sys.stdout.write("="*13)


    # 1) Generar 5000 números utilizando el generador de Mersenne
    sys.stdout.write(u"\nIntegración de Monte Carlo\n")
    f = lambda u: (u*u + 2*math.cos(u))

    random_engine = MersenneTwisterEngine()
    alpha = 3
    beta = 2
    gamma = GammaVariate(alpha, beta, random_engine)

    results = open("exercise3.txt", "w")
    n_results = 1000 # Número de puntos que queremos que saque en el archivo

    n = 1000000 # Número de iteraciones sobre la integral.

    mod_results = int(n/float(n_results))
    sum = 0
    for i in range(1,n+1):
        sum = sum + f(gamma.random())
        if i % mod_results == 0:
            results.write("%s;%s\n" % (i, (sum/float(i))))

    sys.stdout.write(u"Result: %s\n" % (sum/float(n)))
    results.close()


if __name__ == "__main__":
    run()