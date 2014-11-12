#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Simulation(object):
    # Condiciones iniciales
    _minimum_stock = 30
    _max_stock = 100
    _sell_price = 2

    # Simulation events
    _provider_order = None
    _next_client = None

    # stats
    stats = {}

    def __init__(self, client_manger, provider, store, log=None):
        self._client_manager = client_manger
        self._provider = provider
        self._store = store
        self._time = 0
        self._cash = 0
        self._zero_hour = 8
        self._opening_hours = 8

        self._store.set_on_stock_change(self.on_stock_change)
        self._log = log

    def reset(self):
        self._store.reset()
        self._time = 0
        self._cash = 0
        self._provider_order = None
        self._next_client = None
        self.stats = {'clients': {'total': 0, 'fully_served': 0},
                      'stock': [],
                      'cash': []}

    def config(self, minimum_stock, max_stock, opening_hours=8):
        self._minimum_stock = minimum_stock
        self._max_stock = max_stock

        self._zero_hour = 8
        self._opening_hours = 8

        self.reset()

    def write(self, str):
        if self._log:
            self._log(str)
        else:
            print(str)

    def on_stock_change(self, stock):
        if self._store.get_stock() < self._minimum_stock:
            if not self._provider_order:
                price, q, delta_t = self._provider.get_order(self._max_stock - self._store.get_stock())
                self._provider_order = (self._time + delta_t, q, price)
                self.write("\t\tORDER: q=%s\tarrival at hour = %s" % (self._provider_order[1], self._provider_order[0]))

    def get_datetime(self):
        time = self._time + self._zero_hour
        week_day = (self._time % (24*7)) / 24
        day_hour = self._time % 24
        return '%s %s' % (['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][int(week_day)],\
                "{:2.0f}:00".format(day_hour))

    def is_store_open(self):
        # Horarios del almacén
        #   - Apertura: 8 horas al día de lunes a sábado.
        week_day = (self._time % (24*7)) / 24
        day_hour = self._time % 24
        return week_day in xrange(6) and day_hour in xrange(self._opening_hours)

    def next(self):
        if self._time == 0:
            self.write("\n\t=== Hour 0 its considered to be %s (opening time)" % self.get_datetime())

        is_opened = self.is_store_open()
        self.write("\t%s %s\thour: %s\t stock: %s\t cash: %s eur" % (('+' if is_opened else '-'), self.get_datetime(), self._time, self._store.get_stock(), self._cash))

        # Which is going to happen next?
        if self._provider_order or self._next_client:
            # TODO: Si tuviera una lista ordenada con los eventos en el orden en que se van a ir sucediendo...
            t_provider = self._provider_order[0] if self._provider_order else float("inf")
            t_client = self._next_client[0] if self._next_client else float("inf")
            if t_client < t_provider:
                self._handle_client(*self._next_client)
                self._next_client = None
            elif t_provider < t_client:
                self._handle_provider(*self._provider_order)
                self._provider_order = None
            else:
                # TODO: Choose at random which one arrives first
                raise NotImplementedError("Not implemented")

        if not self._next_client:
            next_client, next_request = self._client_manager.get_next()
            self._next_client = (self._time+next_client, next_request)


        # Run until next event
        t_provider = self._provider_order[0] if self._provider_order else float("inf")
        t_client = self._next_client[0] if self._next_client else float("inf")
        t_next_event = min(t_provider, t_client)

        # 1) Stock
        self._cash -= self._store._cost_per_unit * self._store.get_stock() * (t_next_event - self._time)
        self._time = t_next_event

        # 2) Stats
        self.stats['stock'].append((self._time, self._store.get_stock()))
        self.stats['cash'].append((self._time, self._cash))


    def _handle_client(self, t_client, r_client):
        self.write("\t\t%s clients buys %s items" % (1, r_client))
        q = self._store.grab_items(r_client)
        self._cash += q*self._sell_price

        self.stats['clients']['total'] += 1
        if q == r_client:
            self.stats['clients']['fully_served'] += 1

    def _handle_provider(self, price, quantity, t_provider):
        self.write("\t\tprovider: q=%s\tprice=%s" % (quantity, price))
        self._store.put_items(quantity)
        self._cash -= price

    def run(self, max_time):
        while self._time < max_time:
            self.next()

    def run_repeated(self, t_end, n_times):
        # Ejecuta la simulación 'n_times' hasta 't_end' y devuelve un vector con las estadísticas

        stats = []
        for i in xrange(n_times):
            self.reset()
            for j in xrange(t_end):
                self.run(t_end)
            stats.append(self.stats)

        self.reset()
        return stats
