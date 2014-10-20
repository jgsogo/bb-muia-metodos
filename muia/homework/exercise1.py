# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Generación	de números y variables aleatorias.
---------------------------------------------

Utilizando el método del girador de Mersenne obtener una secuencia de 5000 números aleatorios en (0,1)
y estudiar su aleatoriedad utilizando la variante de Knuth del Test de Póker.

Por otro lado, analizar el generador dea Wichmann-Hill y proporcionar una descripción del mismo y
de sus principales características (periodo asociado, aleatoriedad, paquetes estadísticos o entornos
de programación	que lo emplean...).
"""

import time
import sys
import math
from muia.random.mersenne_twister_engine import MersenneTwisterEngine, MUIA_MersenneTwisterEngine
from muia.random.test.poker_knuth import gestionaPokerKnuth as poker_knuth_test


def apply_poker_knuth(generator_class, n=5000, n_series=100):
    generator = generator_class()
    sys.stdout.write("\t\tGenerate %r series of %r random numbers" % (n_series, n))
    t = time.time()
    data = [[generator.random() for i in xrange(n)] for i in xrange(n_series)]
    elapsed = time.time() - t
    sys.stdout.write(" (%.6f seconds)\n" % elapsed)

    xi2 = []
    for series in data:
        xi2.append(poker_knuth_test(listaRegistrosNumeros=series))
    # TODO: ¿Podemos suponer una distribución normal?
    n_xi2 = len(xi2)
    mean = sum(xi2)/n_xi2
    sd = math.sqrt(sum((x-mean)**2 for x in xi2)/n_xi2)
    sys.stdout.write("\t\t+ mean: %s\n" % (mean))
    sys.stdout.write("\t\t+ std dev: %s\n" % (sd))


def run():
    sys.stdout.write("="*10)
    sys.stdout.write("\n== Exercise 1.1\n")
    sys.stdout.write("="*10)


    # 1) Generar 5000 números utilizando el generador de Mersenne
    sys.stdout.write("\n1) Mersenne Twister Engine\n")
    n = 5000
    n_series = 100
    #   - default random.Random (it's Mersenne since 2.x
    sys.stdout.write("\n\t1.1) Mersenne Twister Engine (default Python implementation)\n")
    apply_poker_knuth(MersenneTwisterEngine, n=n, n_series=n_series)

    #   - our implementation of Mersenne Twister
    sys.stdout.write("\n\t1.2) Mersenne Twister Engine (implementation MUIA)\n")
    apply_poker_knuth(MUIA_MersenneTwisterEngine, n=n, n_series=n_series)

    #   - random numbers generated with C++
    sys.stdout.write("\n\t1.2) Mersenne Twister Engine C++ (std::mt19937)\n")
    dir_files = './muia/homework/mersenne_c_files/*'

    class FilePoker():
        file_it = None
        file = None
        i_file = -1

        def __init__(self):
            import glob
            self.files = glob.glob(dir_files)
            if not len(self.files):
                raise AttributeError("There are no files in %r" % dir_files)

        def load_file(self):
            self.i_file += 1
            self.file = self.files[self.i_file]
            filename = "%s" % self.file
            self.file = open(filename, 'r')
            #print "\n\nLoaded: %s" % filename

        def random(self):
            if not self.file:
                self.load_file()

            dato = None
            try:
                dato = float(self.file.readline().strip())
            except ValueError:
                self.file = None
                dato = self.random()
            finally:
                return dato

    apply_poker_knuth(FilePoker, n=n, n_series=n_series)


    # 3) Wichmann-Hill


if __name__ == "__main__":
    run()



