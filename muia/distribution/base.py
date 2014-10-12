# !/usr/bin/env python
# -*- coding: utf-8 -*-


class Distribution(object):
    _engine = None

    def __init__(self, random_engine):
        self._engine = random_engine

    def random(self):
        raise NotImplementedError("Each distribution must provide its generation implementation")