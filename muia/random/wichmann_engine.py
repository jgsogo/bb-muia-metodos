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
