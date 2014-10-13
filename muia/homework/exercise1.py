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

from muia.random import MersenneTwisterEngine
from muia.random.test import PokerKnuth



def run():
    print("="*10)
    print("== Exercise 1.1")
    print("="*10)

    # 1) Generar 5000 números utilizando el generador de Mersene
    n = 5000
    print("\nGenerate %r random numbers using Mersene Twister" % n)
    generator = MersenneTwisterEngine()
    data = [generator.random() for i in xrange(n)]

    # 2) Aplicar el test de póker a este generador

    # 3) Wichmann-Hill


if __name__ == "__main__":
    run()



