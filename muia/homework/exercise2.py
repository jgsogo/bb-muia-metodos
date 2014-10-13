# !/usr/bin/env python
# -*- coding: utf-8 -*-

import math

from muia.random import MersenneTwisterEngine
from muia.distribution import PoissonVariate, DiscreteVariate, NormalVariate

from .warehouse.client_manager import ClientManager
from .warehouse.provider import Provider
from .warehouse.store import Store
from .warehouse.simulation import Simulation


def get_client_manager(random_engine):
    client_manager = ClientManager(random_engine)

    # Llegada de clientes: proceso de Poisson(0,5)
    lambd = 0.5
    client_manager.set_arrival(PoissonVariate, lambd=lambd)
    print("\t - Arrivals: poisson distribution with lambda=%r" % lambd)

    # Cantidad pedida por cada cliente: muestreo discreta
    client_manager.set_demand(DiscreteVariate, prob_list=[(0.3, 1), (0.4, 2), (0.2, 3), (0.1, 4)])
    print("\t - Demand: discrete distribution")

    return client_manager

def get_provider(random_engine):
    class ProviderAgreement(Provider):
        # Descuento por retraso
        def get_order(self, quantity):
            base_price, q, t = super(ProviderAgreement, self).get_order(quantity)
            # TODO: No queda clara la redacción del ejercicio, ¿qué pasa con las fracciones de tres horas?
            delay_mod = int(math.fabs(t - 48)) / 3
            if delay_mod != 0:
                delta_price = base_price * delay_mod * 0.01
                base_price = base_price + delta_price if t > 48. else base_price - delta_price
            return base_price, q, t

    provider = ProviderAgreement(random_engine)
    print("\t - Prices:\t10 + 1*q [q < 50]\n\t\t\t10 + 0.75*q [q >= 50]")
    provider.set_unit_cost(10, 1)
    provider.set_offer(50, 0.75)

    mu = 48
    sigma = 0.8
    print("\t - Serve time: N(%s,%s)" % (mu, sigma))
    provider.set_order_time(NormalVariate, mu=mu, sigma=sigma)

    return provider


def run():
    print("="*16)
    print("=== Exercise 1.2")
    print("="*16)

    # 0) Inicializar el generador de números aleatorios
    print("\n\tInitialize unique random generator: MerseneTwister")
    seed = 12345
    print("\t - seed: %s" % seed)
    random_engine = MersenneTwisterEngine()
    random_engine.seed(seed)

    # 1) Construir el gestor de clientes
    print("\n\tBuild client manager")
    clients = get_client_manager(random_engine)

    # 2) Construir el proveedor
    print("\n\tBuild provider")
    provider = get_provider(random_engine)

    # 3) Construir el propio almacén
    initial = 70
    cost_per_unit = 0.0001
    print("\n\tBuild warehouse")
    print("\t - Initial stock: %s" % initial)
    print("\t - Store cost per unit: %s" % cost_per_unit)
    store = Store(initial_stock=initial)
    store.set_cost_per_unit(cost_per_unit)

    # 4) Simulation framework
    print("\n\tBuild simulation framework")
    sim = Simulation(clients, provider, store)
    sim.config()

    for i in xrange(5*30*24):
        sim.run(1)

    # 5) Print stats
    print("\n\tStats")
    from pprint import pprint
    print("\t - Total clients: %s" % sim.stats['clients']['total'])
    print("\t   + fully served: %s" % sim.stats['clients']['fully_served'])
    print("\t - Mean stock: %s" % (sum([it[1] for it in sim.stats['stock']])/len(sim.stats['stock'])))


if __name__ == "__main__":
    run()