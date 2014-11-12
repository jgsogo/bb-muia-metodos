# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random


class MUIA_MersenneTwisterEngine(random.Random):
    # Period parameters
    N = 624
    M = 397
    MATRIX_A = 0x9908b0dfL      # Constant vector a
    UPPER_MASK = 0x80000000L    # most significant w-r bits
    LOWER_MASK = 0x7fffffffL    # least significant r bits

    # Tempering parameters
    TEMPERING_MASK_B = 0x9d2c5680L
    TEMPERING_MASK_C = 0xefc60000L

    def TEMPERING_SHIFT_U(self, y):
        return y >> 11

    def TEMPERING_SHIFT_S(self, y):
        return y << 7

    def TEMPERING_SHIFT_T(self, y):
        return y << 15

    def TEMPERING_SHIFT_L(self, y):
        return y >> 18

    def __init__(self, seed=4357):
        self.mt = []        # the array for the state vector
        self.mti = self.N+1 # mti==N+1 means mt[N] is not initialized
        self._seed = seed

    def sgenrand(self, seed):
        # setting initial seeds to mt[N] using
        # the generator Line 25 of Table 1 in
        # [KNUTH 1981, The Art of Computer Programming
        #    Vol. 2 (2nd Ed.), pp102]
        self.mt = []
        self.mt.append(seed & 0xffffffffL)
        for self.mti in xrange(1, self.N+1):
            self.mt.append((69069*self.mt[self.mti-1]) & 0xffffffffL)

    def genrand(self):
        mag01 = [0x0L, self.MATRIX_A]
        # mag01[x] = x * MATRIX_A  for x=0,1
        y = 0

        if self.mti >= self.N: # generate N words at one time
            kk = 0

            if self.mti == self.N+1:        # if sgenrand() has not been called,
                self.sgenrand(self._seed)   # a default initial seed is used

            for kk in xrange((self.N-self.M) + 1):
              y = (self.mt[kk]&self.UPPER_MASK)|(self.mt[kk+1]&self.LOWER_MASK)
              self.mt[kk] = self.mt[kk+self.M] ^ (y >> 1) ^ mag01[y & 0x1]

            for kk in xrange(kk, self.N):
              y = (self.mt[kk]&self.UPPER_MASK)|(self.mt[kk+1]&self.LOWER_MASK)
              self.mt[kk] = self.mt[kk+(self.M-self.N)] ^ (y >> 1) ^ mag01[y & 0x1]

            y = (self.mt[self.N-1]&self.UPPER_MASK)|(self.mt[0]&self.LOWER_MASK)
            self.mt[self.N-1] = self.mt[self.M-1] ^ (y >> 1) ^ mag01[y & 0x1]

            self.mti = 0

        y = self.mt[self.mti]
        self.mti += 1
        y ^= self.TEMPERING_SHIFT_U(y)
        y ^= self.TEMPERING_SHIFT_S(y) & self.TEMPERING_MASK_B
        y ^= self.TEMPERING_SHIFT_T(y) & self.TEMPERING_MASK_C
        y ^= self.TEMPERING_SHIFT_L(y)

        return ( float(y) / 0xffffffffL ) # reals
        # return y  # for integer generation


    def random(self):
        return self.genrand()

    def seed(self):
        pass

    def getstate(self):
        pass

    def setstate(self):
        pass

    def jumpahead(self):
        pass


if os.getenv('USES_MUIA'):
    MersenneTwisterEngine = MUIA_MersenneTwisterEngine
else:
    # TODO: Check Python version, it may be still using Wichmann-Hill (Python < 2.3)
    MersenneTwisterEngine = random.Random



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