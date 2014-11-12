# !/usr/bin/env python
# -*- coding: utf-8 -*-

import math

from muia.random import MersenneTwisterEngine
from muia.distribution import PoissonVariate, DiscreteVariate, NormalVariate

from .warehouse.client_manager import ClientManager
from .warehouse.provider import Provider
from .warehouse.store import Store
from .warehouse.simulation import Simulation


def build_client_manager(random_engine):
    client_manager = ClientManager(random_engine)

    # Llegada de clientes: proceso de Poisson(0,5)
    lambd = 0.5
    client_manager.set_arrival(PoissonVariate, lambd=lambd)
    print("\t - Arrivals: poisson distribution with lambda=%r" % lambd)

    # Cantidad pedida por cada cliente: muestreo discreta
    client_manager.set_demand(DiscreteVariate, prob_list=[(0.3, 1), (0.4, 2), (0.2, 3), (0.1, 4)])
    print("\t - Demand: discrete distribution")

    return client_manager

def build_provider(random_engine):
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


def normal_distribution(data):
    n = len(data)
    mean = sum(data)/n
    sd = math.sqrt(sum((x-mean)**2 for x in data)/n)
    return (mean, sd)

def mean_stats(data):
    # 5) Print stats
    total_clients = normal_distribution([it['clients']['total'] for it in data])
    fully_served = normal_distribution([it['clients']['fully_served'] for it in data])
    closed_clients = normal_distribution([it['clients']['closed'] for it in data])
    mean_stock = normal_distribution([sum([it2[1] for it2 in it['stock']])/len(it['stock']) for it in data])
    expected_revenue = normal_distribution([it['cash'][-1][1] for it in data])
    t_empty_stock = normal_distribution([it['t_empty_stock'] for it in data])
    lost_sells = normal_distribution([it['lost_sells'] for it in data])
    return total_clients, fully_served, closed_clients, mean_stock, expected_revenue, t_empty_stock, lost_sells


def case_A(seed, sim_log=None):
    print("\n\n*** Exercise 1.2.a")
    print("*"*18)

    # 0) Inicializar el generador de números aleatorios
    print("\n\tInitialize unique random generator: MerseneTwister")
    print("\t - seed: %s" % seed)
    random_engine = MersenneTwisterEngine()
    random_engine.seed(seed)

    # 1) Construir el gestor de clientes
    print("\n\tBuild client manager")
    clients = build_client_manager(random_engine)

    # 2) Construir el proveedor
    print("\n\tBuild provider")
    provider = build_provider(random_engine)

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
    minimum_stock = 30
    max_stock = 100
    print("\t - Minimum stock: %s" % minimum_stock)
    print("\t - Maximum stock: %s" % max_stock)
    def pp(str):
        if sim_log: print(str)
        else: pass
    sim = Simulation(clients, provider, store, pp)
    sim.config(minimum_stock=minimum_stock, max_stock=max_stock)

    n_times = 100
    t_end = 5*30*24
    data = sim.run_repeated(t_end, n_times)

    # 5) Print stats
    total_clients, fully_served, closed_clients, mean_stock, expected_revenue, t_empty_stock, lost_sells = mean_stats(data)
    print("\n\tStats (simulated %s times)" % n_times)
    print("\t - Hours simulated:\t%s hours" % t_end)
    print("\t - Total clients:\t%s\t(rms=%s)" % (total_clients[0], total_clients[1]))
    print("\t   + fully served:\t%s\t(rms=%s)" % (fully_served[0], fully_served[1]))
    print("\t   + closed clients:\t%s\t(rms=%s)" % (closed_clients[0], closed_clients[1]))
    print("\t - Mean stock:\t%s\t(rms=%s)" % (mean_stock[0], mean_stock[1]))
    print("\t - Expected revenue:\t%s eur\t(rms=%s)" % (expected_revenue[0], expected_revenue[1]))
    print("\t - Empty stock time:\t%s hours\t(rms=%s)" % (t_empty_stock[0], t_empty_stock[1]))
    print("\t - Lost sells:\t%s\t(rms=%s)" % (lost_sells[0], lost_sells[1]))


def case_B(seed):
    print("\n\n*** Exercise 1.2.b")
    print("*"*18)
    # TODO: Se trata de sacar gráficas


def case_C(seed):
    print("\n\n*** Exercise 1.2.c")
    print("*"*18)

    random_engine = MersenneTwisterEngine()
    random_engine.seed(seed)
    print("\n\tBuild client manager")
    clients = build_client_manager(random_engine)
    print("\n\tBuild provider")
    provider = build_provider(random_engine)

    initial = 70
    cost_per_unit = 0.0001
    store = Store(initial_stock=initial)
    store.set_cost_per_unit(cost_per_unit)

    sim = Simulation(clients, provider, store, lambda u: None)


    # Análisis de sensibilidad de la solución
    stock_step = 5
    n_times = 10
    t_end = 5*30*24

    # 1) Playing with stocks
    max_max_stock = 150
    min_min_stock = 0

    maximum_revenue = (-1, -1, -1, -1, -1, -1, -1, -1)
    #all_data_stock = {}
    f = open('stock_map.txt', 'w')

    print("\n\tSimulate! (%s times each scenario)" % n_times)
    for max_stock in range(min_min_stock, max_max_stock+1, stock_step):
        for min_stock in range(min_min_stock, max_stock+1, stock_step):
            random_engine.seed(seed) # Reset random
            sim.config(minimum_stock=min_stock, max_stock=max_stock)

            data = sim.run_repeated(t_end, n_times)
            #total_clients, fully_served, mean_stock, expected_revenue = mean_stats(data)
            total_clients, fully_served, closed_clients, mean_stock, expected_revenue, t_empty_stock, lost_sells = mean_stats(data)

            if expected_revenue[0] > maximum_revenue[2]:
                maximum_revenue = (min_stock, max_stock, expected_revenue[0], fully_served[0], closed_clients[0], total_clients[0], t_empty_stock[0], lost_sells[0])

            print("\t - stock: [%s, %s]\t revenue: %s\t stock (mean): %s\t served: %s%%" %
              (min_stock, max_stock,
               "{:2.2f}".format(expected_revenue[0]),
               mean_stock[0],
               "{:2.2f}".format(fully_served[0]/float(total_clients[0]-closed_clients[0])*100)))

            #all_data_stock.update({(min_stock, max_stock): data})
            f.write("%s,%s,%s,%s,%s,%s,%s,%s\n" % (min_stock, max_stock, expected_revenue[0], total_clients[0], fully_served[0], closed_clients[0], t_empty_stock[0], lost_sells[0]))
    print("\tMaximum revenue is %r with stock in [%s, %s]" % ("{:2.2f}".format(maximum_revenue[2]), maximum_revenue[0], maximum_revenue[1]))
    f.close()

    # 5) Print stats
    print("\n\tStats (for max_revenue)")
    print("\t - Hours simulated:\t%s hours" % t_end)
    print("\t - Total clients:\t%s\t(rms=%s)" % (maximum_revenue[5], '~'))
    print("\t   + fully served:\t%s\t(rms=%s)" % (maximum_revenue[3], '~'))
    print("\t   + closed clients:\t%s\t(rms=%s)" % (maximum_revenue[4], '~'))
    print("\t - Mean stock:\t%s\t(rms=%s)" % ('~', '~'))
    print("\t - Expected revenue:\t%s\t(rms=%s)" % (maximum_revenue[2], '~'))
    print("\t - Empty stock time:\t%s hours\t(rms=%s)" % (maximum_revenue[6], '~'))
    print("\t - Lost sells:\t%s\t(rms=%s)" % (maximum_revenue[7], '~'))

    """
    max_stats = all_data_stock[(maximum_revenue[1], maximum_revenue[2])]
    total_clients, fully_served, mean_stock, expected_revenue = mean_stats(max_stats)
    print("\n\tStats (for max_revenue)")
    print("\t - Hours simulated:\t%s hours" % t_end)
    print("\t - Total clients:\t%s\t(rms=%s)" % (total_clients[0], total_clients[1]))
    print("\t   + fully served:\t%s\t(rms=%s)" % (fully_served[0], fully_served[1]))
    print("\t - Mean stock:\t%s\t(rms=%s)" % (mean_stock[0], mean_stock[1]))
    print("\t - Expected revenue:\t%s\t(rms=%s)" % (expected_revenue[0], expected_revenue[1]))
    """



def run():
    print("="*16)
    print("=== Exercise 1.2")
    print("="*16)

    seed = 12345
    case_A(seed)
    case_B(seed)
    case_C(seed)


if __name__ == "__main__":
    run()