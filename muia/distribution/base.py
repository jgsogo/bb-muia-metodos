# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Distribution(object):
    _engine = None

    def __init__(self, engine_class, seed=None):
        self._engine = engine_class() if engine_class else random.Random()
        if seed:
            self._engine.seed(seed)

    def random(self):
        raise NotImplementedError("Each distribution must provide its generation implementation")