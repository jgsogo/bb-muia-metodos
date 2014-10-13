# !/usr/bin/env python
# -*- coding: utf-8 -*-


from muia.random import MersenneTwisterEngine
from muia.distribution import PoissonVariate, DiscreteVariate
from .warehouse.client_manager import ClientManager


def get_client_manager(random_engine):
    """
    La llegada de clientes al almacén se distribuye según un proceso de Poisson de parámetro
    λ = 0.5 clientes por hora y la cantidad de productos demandados por cada uno de ellos
    tiene la siguiente distribución:
    """

    client_manager = ClientManager(random_engine)

    # Llegada de clientes: proceso de Poisson(0,5)
    lambd = 0.5
    client_manager.set_arrival(PoissonVariate, lambd=lambd)
    print("\t - Arrivals: poisson distribution with lambda=%r" % lambd)

    # Cantidad pedida por cada cliente: muestreo discreta
    client_manager.set_demand(DiscreteVariate, prob_list=[(0.3, 1), (0.4, 2), (0.2, 3), (0.1, 4)])
    print("\t - Demand: discrete distribution")

    return client_manager


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


if __name__ == "__main__":
    run()