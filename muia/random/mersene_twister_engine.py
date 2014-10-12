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
