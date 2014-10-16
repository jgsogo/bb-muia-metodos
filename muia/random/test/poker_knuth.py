# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'jonathan'

def imprime(dato,formato = " %s "):
    print (formato % dato)

def printMatrix(a):
    for i in range(len(a)):
        fila =""
        for j in a[i]:
            fila = fila + " " + str(j)
        print(fila)

def transformaEnteros ( numero):
    ### Recibe un numero, en el rango [0, 1] y retorna su correspondiente en el rango [1 , 10]####
    if numero > 1 :
        return numero+2
    elif numero >= 0 and numero < 0.1 :
        return 1
    elif numero >= 0.1 and numero < 0.2 :
        return 2
    elif numero >= 0.2 and numero < 0.3 :
        return 3
    elif numero >= 0.3 and numero < 0.4 :
        return 4
    elif numero >= 0.4 and numero < 0.5 :
        return 5
    elif numero >= 0.5 and numero < 0.6 :
        return 6
    elif numero >= 0.6 and numero < 0.7 :
        return 7
    elif numero >= 0.7 and numero < 0.8 :
        return 8
    elif numero >= 0.8 and numero < 0.9 :
        return 9
    elif numero >= 0.9 and numero <= 1 :
        return 10
    else:
        return numero

def remueveNApariciones(lista,elemento):
    ### Funcion auxiliar que elimina los primeros elementos de una lista
    # cuando sean iguales al elemento###
    if len(lista)==0:
        return lista
    elif lista[0] == elemento:
        lista.remove(elemento)
        return remueveNApariciones(lista,elemento)
    else:
        return lista

def cuentaNumeroDeEliminacionesAntesVacio(lista):
    ### Funcion que cuenta el numero de valores diferentes en una lista
    # print ("pruebas para la funcion cuentaNumeroDeEliminacionesAntesVacio() ")
    # print ("caso 1: lista = [ 5, 5, 5, 1, 1] ")
    # lista = [ 5, 5, 5, 1, 1]
    # print ("Cuenta las categorias %d " % cuentaNumeroDeEliminacionesAntesVacio(lista) )
    # print ("caso 2: lista = [ 2, 2, 2, 2, 2] ")
    # lista = [ 2, 2, 2, 2, 2]
    # print ("Cuenta las categorias %d " % cuentaNumeroDeEliminacionesAntesVacio(lista) )
    # print ("caso 3: lista = [ 2 ] ")
    # lista = [ 2 ]
    # print ("Cuenta las categorias %d " % cuentaNumeroDeEliminacionesAntesVacio(lista) )
    # print ("caso 4: lista = [ ] ")
    # lista = [ ]
    # print ("Cuenta las categorias %d " % cuentaNumeroDeEliminacionesAntesVacio(lista) )
    # print ("caso 5: lista = [ 1, 2, 3, 4, 5 ] ")
    # lista = [ 1, 2, 3, 4, 5 ]
    # print ("Cuenta las categorias %d " % cuentaNumeroDeEliminacionesAntesVacio(lista) )
    #  ###
    conteo=0
    copiaLista = lista[:]
    copiaLista.sort()
    while len(copiaLista) > 0:
        elemento = copiaLista[0]
        copiaLista = remueveNApariciones(copiaLista,elemento)
        conteo = (conteo + 1)
        if len(copiaLista) == 0:
            break
    return conteo

def cuentaFrecuencias( nuevaCategoria, listaFrecuencias):
    ###Incrementa la frecuencia en una categoria y si esta categoria es mayor a las existentes,
    # aumenta el tamano hasta que se pueda inicializar a 1, como frecuencia en esa categoria.
    #
    # Pruebas # print ("pruebas para la funcion cuentaFrecuencias() ")
    # print ("caso 1: frecuencias = [ 0, 1, 2 ,70 ]; catego = 10 ")
    # frecuencias = [ 0, 1, 2 ,70 ]
    # catego = 10
    # cuentaFrecuencias(catego,frecuencias)
    # map( imprime, frecuencias)
    # print ("caso 2: frecuencias = [ ]; catego = 5 ")
    # frecuencias = [  ]
    # catego = 5
    # cuentaFrecuencias(catego,frecuencias)
    # map( imprime, frecuencias)
    # print ("caso 3: frecuencias = [ 0, 0, 0, 0, 1 ]; catego = 5 ")
    # frecuencias = [ 0, 0, 0, 0, 1 ]
    # catego = 5
    # cuentaFrecuencias(catego,frecuencias)
    # map( imprime, frecuencias)
    # print ("caso 4: frecuencias = [ 2 , 3 ]; catego = 1 ")
    # frecuencias = [ 2, 3 ]
    # catego = 1
    # cuentaFrecuencias(catego,frecuencias)
    # map( imprime, frecuencias)
    ###

    if len(listaFrecuencias) < nuevaCategoria :
        diferencia = nuevaCategoria - len(listaFrecuencias)
        while diferencia > 0:
            elemento = 0
            if diferencia == 1:
                elemento =1
            listaFrecuencias.append(elemento)
            diferencia = diferencia -1
    else:
        listaFrecuencias[nuevaCategoria -1] = listaFrecuencias[nuevaCategoria -1]+1

def funcionTroceaLista(tamanoTrozo,lista):
    ### Funcion retorna una matriz, dada una lista y un numero
    #    que sera el tamano de las sublista,
    #    funcion necesaria para
    #    print ("pruebas para la funcion funcionTroceaLista(tamanoTrozo,lista) ")
    #    print ("caso -1: mi_lista = [ 0, 1, 2 ]; elTamanoTrozo = 5 ")
    #    mi_lista = [ 0, 1, 2 ]
    #    elTamanoTrozo = 5
    #    matriz = funcionTroceaLista(elTamanoTrozo,mi_lista)
    #    printMatrix(matriz)
    #    print ("caso 0: mi_lista = [ 0, 1, 2 ]; elTamanoTrozo = 3 ")
    #    mi_lista = [ 0, 1, 2 ]
    #    elTamanoTrozo = 3
    #    matriz = funcionTroceaLista(elTamanoTrozo,mi_lista)
    #    printMatrix(matriz)
    #    print ("caso 1: mi_lista = [ 0, 1, 2 ,70 ]; elTamanoTrozo = 2 ")
    #    mi_lista = [ 0, 1, 2 ,70,4 ]
    #    elTamanoTrozo = 3
    #    matriz = funcionTroceaLista(elTamanoTrozo,mi_lista)
    #    printMatrix(matriz)
    #    print ("caso 2: mi_lista = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ]; elTamanoTrozo = 1 ")
    #    mi_lista = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ]
    #    elTamanoTrozo = 1
    #    matriz = funcionTroceaLista(elTamanoTrozo,mi_lista)
    #    printMatrix(matriz)
    #    print ("caso 3: mi_lista = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ]; elTamanoTrozo = 3 ")
    #    mi_lista = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ]
    #    elTamanoTrozo = 3
    #    matriz = funcionTroceaLista(elTamanoTrozo,mi_lista)
    #    printMatrix(matriz)
    #    print ("caso 4: mi_lista = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ]; elTamanoTrozo = 5 ")
    #    mi_lista = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ]
    #    elTamanoTrozo = 5
    #    matriz = funcionTroceaLista(elTamanoTrozo,mi_lista)
    #    printMatrix(matriz)
    ###
    salida = []
    aux = []
    if len(lista) == 0:
        return [ [] ] #Matriz con una lista vacia
    if len(lista) < tamanoTrozo :
        return [ lista ] #Matriz con la misma lista de entrada aunque menor al tamano sugerido
    else:
        indice = 0
        while len(lista) >= indice:
            if len(lista) == indice:
                salida.append(aux[:])
            elif indice % tamanoTrozo == 0 and indice != 0:
                salida.append(aux[:])
                aux = [lista[indice]]
            else:
                aux.append( lista[ indice ] )
            indice = indice+1

    return salida

def gestionaPokerKnuth(ficheroRegistrosNumeros=None,listaRegistrosNumeros=None):
    infile = None
    lineas = None
    clases = 5
    if ficheroRegistrosNumeros == None and listaRegistrosNumeros==None :
        imprime("Imposible empezar sin la entrada de numeros en lista o fichero"," %s ")
    elif ficheroRegistrosNumeros != None:
        imprime( "Calculando el Poker_knuth a partir de un fichero como entrada", " %s " )
        infile = open(ficheroRegistrosNumeros, "r");
        lineas = infile.readlines()
    elif listaRegistrosNumeros != None :
        imprime("Calculando el Poker_Knuth a partir de una lista como entrada"," %s ")
        lineas = listaRegistrosNumeros[:]

    numeros = map(float,lineas )
    numerosTrans = map(transformaEnteros,numeros )
    matriz = funcionTroceaLista(clases,numerosTrans)
    listaCategorias = []
    for sublista in matriz:
        listaCategorias.append( cuentaNumeroDeEliminacionesAntesVacio(sublista) )
    frecuenciasObservadas=[]
    #imprime("******* inicio categorias ********")
    for categoria in listaCategorias:
    #    imprime( categoria )
        cuentaFrecuencias( categoria, frecuenciasObservadas )
    #imprime("******* Fin categorias ********")

    map( imprime , frecuenciasObservadas )

    ###Voy por aqui!!!
    ###TODO  Falta Sumatoria de ((FrecuenciaObservada - FrecuenciaEsperada) 2) / FrecuenciaEsperada
    ### El grado de libertad: k - r - 1 = 5 - 0 - 1 = 4
    ###TODO Comparar con tabla X 2
    ###TODO Evaluar la hipotesis de Poker_Knuth .Con cual probabilidad?



    if ficheroRegistrosNumeros != None:
        # Cerramos el fichero.
        infile.close();

direccion_fichero = "C:/Users/Jonathan/Google Drive/Master/Metodos de simulacion/practicas/practica 1/poker/ejemplos.txt"
gestionaPokerKnuth( ficheroRegistrosNumeros=direccion_fichero)
