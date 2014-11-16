# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random

try:
    WichmannHill = random.WichmannHill
except AttributeError:

    # TODO: Implementarlo, si puntua...
    class WichmannHill(random.Random):

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

    generator = WichmannHill()
    numbers = [generator.random() for i in range(n)]
    from .test.poker_knuth import gestionaPokerKnuth
    result = gestionaPokerKnuth(listaRegistrosNumeros=numbers)
    print result


if __name__ == "__main__":
    test_poker_knuth()