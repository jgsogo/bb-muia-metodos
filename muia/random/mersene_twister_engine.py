# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random

try:
    MersenneTwisterEngine = random.Random
except ImportError:

    # TODO: Implementarlo, si puntua...
    class MersenneTwisterEngine(random.Random):

        def random(self):
            pass

        def seed(self):
            pass

        def getstate(self):
            pass

        def setstate(self):
            pass

        def jumpahead(self):
            pass



def test_poker_knuth(n=5000):
    print("Test de poker. Variante Knuth")
    print("\t - random sample size: %s" % n)

    generator = MersenneTwisterEngine()
    numbers = [generator.random() for i in range(n)]
    from .test.poker_knuth import gestionaPokerKnuth
    result = gestionaPokerKnuth(listaRegistrosNumeros=numbers)
    print result


if __name__ == "__main__":
    print("="*16)
    print("==== MersenneTwisterEngine")
    print("="*16)
    test_poker_knuth()