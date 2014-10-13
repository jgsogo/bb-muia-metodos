#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Simulation(object):
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
        return '%s %s' % (['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][week_day],\
                "{:2.0f}:00".format(day_hour))

    def is_store_open(self):
        # Horarios del almacén
        #   - Apertura: 8 horas al día de lunes a sábado.
        week_day = (self._time % (24*7)) / 24
        day_hour = self._time % 24
        return week_day in xrange(6) and day_hour in xrange(self._opening_hours)

    def run(self, step):
        if self._time == 0:
            self.write("\n\t=== Hour 0 its considered to be %s (opening time)" % self.get_datetime())

        is_opened = self.is_store_open()
        self.write("\t%s %s\thour: %s\t stock: %s\t cash: %s eur" % (('+' if is_opened else '-'), self.get_datetime(), self._time, self._store.get_stock(), self._cash))

        # Receive provider orders
        # TODO: ¿Recibimos proveedores incluso cuando el almacén está cerrado? ¿el stock antes o después de medir?
        if self._provider_order and self._provider_order[0] <= self._time:
            self.write("\t\tprovider: q=%s\tprice=%s" % (self._provider_order[1], self._provider_order[2]))
            self._store.put_items(self._provider_order[1])
            self._cash -= self._provider_order[2]
            self._provider_order = None

        # Manage clients for this hour
        if is_opened:
            n_clients, request = self._client_manager.next_hour() # TODO: Si atiendo primero a los clientes con menor petición cumple con las órdenes de más clientes...
            if n_clients:
                self.write("\t\t%s clients buys %s items" % (n_clients, request))
                for it in request:
                    q = self._store.grab_items(it)
                    self._cash += q*self._sell_price

                    self.stats['clients']['total'] += 1
                    if q == it:
                        self.stats['clients']['fully_served'] += 1

        # Stock
        self._cash -= self._store._cost_per_unit * self._store.get_stock()

        self.stats['stock'].append((self._time, self._store.get_stock()))
        self.stats['cash'].append((self._time, self._cash))

        # Increment time and return
        next_time = self._time + step # TODO: Tener claro si avanzo el tiempo antes o después de simular.
        self._time = next_time


    def run_repeated(self, t_end, n_times, t_step=1):
        # Ejecuta la simulación 'n_times' hasta 't_end' y devuelve un vector con las estadísticas

        stats = []
        for i in xrange(n_times):
            self.reset()
            for j in xrange(t_end):
                self.run(t_step)
            stats.append(self.stats)

        self.reset()
        return stats

