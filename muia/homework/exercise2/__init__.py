# !/usr/bin/env python
# -*- coding: utf-8 -*-


from muia.distribution.poisson_variate import PoissonVariate, DiscreteVariate
from .client_manager import ClientManager


def get_client_manager(random_engine):
    """
    La llegada de clientes al almacén se distribuye según un proceso de Poisson de parámetro
    λ = 0.5 clientes por hora y la cantidad de productos demandados por cada uno de ellos
    tiene la siguiente distribución:
    """

    client_manager = ClientManager(random_engine)
    # Llegada de clientes: proceso de Poisson(0,5)
    client_manager.set_arrival(PoissonVariate, lambd=0.5)
    # Cantidad pedida por cada cliente: muestreo discreta
    client_manager.set_demand(DiscreteVariate, prob_list=[(0.3, 1), (0.4, 2), (0.2, 3), (0.1, 4)])

    return client_manager