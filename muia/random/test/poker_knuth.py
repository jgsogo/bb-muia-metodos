# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'jonathan'
import sys


class PokerKnuth(object):
    _significacion = 0.950 # (5%)
    _chi2_significacion = 9.488

    def __init__(self, chi2_file, verbosity=2):
        self._chi2_file = chi2_file
        self._verbosity = verbosity

    def imprime(self, dato, formato = " %s ", end='\n'):
        if self._verbosity >= 1:
            sys.stdout.write((formato + end) % dato)

    def printMatrix(self, a):
        for i in range(len(a)):
            fila =""
            for j in a[i]:
                fila = fila + " " + str(j)
            print(fila)

    def transformaEnteros (self, numero):
        ### Recibe un numero, en el rango [0, 1] y retorna su correspondiente en el rango [1 , 10]####
        if numero >= 0 and numero < 0.1 :
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
        elif numero >= 0.9 and numero < 1 : # TODO: ¿numero==1 es un valor válido?
            return 10
        else:
            raise AttributeError("Value %r not in range [0, 1)" % numero)


    def remueveNApariciones(self, lista,elemento):
        ### Funcion auxiliar que elimina los primeros elementos de una lista
        # cuando sean iguales al elemento###
        if len(lista)==0:
            return lista
        elif lista[0] == elemento:
            lista.remove(elemento)
            return self.remueveNApariciones(lista,elemento)
        else:
            return lista

    def cuentaNumeroDeEliminacionesAntesVacio(self, lista):
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
            copiaLista = self.remueveNApariciones(copiaLista,elemento)
            conteo = (conteo + 1)
            if len(copiaLista) == 0:
                break
        return conteo

    def cuentaFrecuencias(self, nuevaCategoria, listaFrecuencias):
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

    def funcionTroceaLista(self, tamanoTrozo,lista):
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

    def calculaFrecuenciaEsperada(self, n_iteraciones,categoria):
        ### Estima la frecuencia esperada dada una categoria y un numero de observaciones realizadas
        #  Se espera que el numero de la categoria se ubique entre [1 , 5]
        # ###
        probabilidadesPorCategoria = [ 0.0001 ,0.0135 ,0.18 ,0.504,0.3024 ]
        return (n_iteraciones*probabilidadesPorCategoria[categoria-1])

    def cargaTablaChiCuadrado(self, cuartil, fichero_chi):
        tablaChi = []
        infile = open(fichero_chi, "r");
        lineas = infile.readlines()

        cuentaFilas=0

        for linea in lineas:
            # imprime("**** imprime lineas *****")
            # imprime(linea)
            aux= linea.split(";")
            auxFloat = []
            for dato in aux:
                # imprime("**** imprime datos *****")
                # imprime(dato," %s ")
                if cuentaFilas == 0 : #Las cabeceras de la tabla
                    cuartil.append( dato )
                else:
                    auxFloat.append( dato )
            if cuentaFilas != 0 : #Las NO cabeceras de la tabla
                map( float, auxFloat)
                tablaChi.append( auxFloat )
            cuentaFilas = cuentaFilas+1

        #printMatrix( tablaChi )
        infile.close()
        return tablaChi

    def getIndiceGradoLibertad(self, cabeceras_cuartil,x1_a):
        indice =0
        for dato in cabeceras_cuartil:
            if dato == x1_a:
                return indice
            indice = indice+1
        indice =-1
        return indice

    def getCuartil(self,chiObservado,gradoLibertad,tablaChi):
        ### En caso que no se acepte el chiObservado porque sea menor a los chiTeoricos, se retorna -1 como indice###
        chiTeoricosParaMiGrado = tablaChi[ gradoLibertad-1 ][1:] #El primer valor de la fila se corresponde al grado de libertad, por eso no lo queremos
        esHayado=False
        indiceUltimoMayor=0 #Será el indice del maximo alpha para el que se acepta el chiObservado
        for chiTeorico in chiTeoricosParaMiGrado:
#            self.imprime("Valor a comparar")
 #           self.imprime(chiTeorico,formato =" %s ")
            if float(chiTeorico) >= chiObservado:
                esHayado=True
                break
            indiceUltimoMayor = indiceUltimoMayor+1
        if not esHayado :
            indiceUltimoMayor = -1
        return indiceUltimoMayor


    def gestionaPokerKnuth(self, ficheroRegistrosNumeros=None,listaRegistrosNumeros=None):
        self.imprime("")
        infile = None
        lineas = None
        clases = 5
        if not self._chi2_file:
            self.imprime("Imposible empezar sin la tabla chi2")
            return -1
        if ficheroRegistrosNumeros == None and listaRegistrosNumeros==None :
            self.imprime("Imposible empezar sin la entrada de numeros en lista o fichero"," %s ")
            return -1
        elif ficheroRegistrosNumeros != None:
            self.imprime( "Calculando el Poker_knuth a partir de un fichero como entrada", " %s " )
            infile = open(ficheroRegistrosNumeros, "r");
            lineas = infile.readlines()
            infile.close()
        elif listaRegistrosNumeros != None :
            self.imprime("Calculando el Poker_Knuth a partir de una lista como entrada"," %s ")
            lineas = listaRegistrosNumeros[:]

        numeros = map(float,lineas )
        if len(numeros) <= 50:
            raise AttributeError(u"Need at least 50 samples to perform Knuth\'s Poker Test")

        self.imprime(u"Muestra: %s elementos" % len(numeros))

        numerosTrans = map(self.transformaEnteros,numeros )
        matriz = self.funcionTroceaLista(clases,numerosTrans)
        listaCategorias = []
        for sublista in matriz:
            listaCategorias.append( self.cuentaNumeroDeEliminacionesAntesVacio(sublista) )
        frecuenciasObservadas=[]
        #imprime("******* inicio categorias ********")
        for categoria in listaCategorias:
        #    imprime( categoria )
            self.cuentaFrecuencias( categoria, frecuenciasObservadas )
        #imprime("******* Fin categorias ********")

        #map( self.imprime , frecuenciasObservadas )


        n_iteraciones = 0
        for valor in frecuenciasObservadas:
            n_iteraciones = (n_iteraciones+ valor)

        i_esima_categoria =1
        chi_cuadrado = 0
        frecuenciaEsperadaAux=0

        data = []
        for frecuenciaCategoria in frecuenciasObservadas:
            frecuenciaEsperadaAux=self.calculaFrecuenciaEsperada(n_iteraciones,i_esima_categoria)

            aux_discrepancia = (frecuenciaCategoria - frecuenciaEsperadaAux)**2/float(frecuenciaEsperadaAux)
            chi_cuadrado += aux_discrepancia

            data.append((i_esima_categoria, frecuenciaCategoria, frecuenciaEsperadaAux, aux_discrepancia))
            i_esima_categoria = (i_esima_categoria+1)

        self.imprime("\n=== FRECUENCIAS")
        self.imprime("Clase\tfreq observada\tfreq esperada\tdiscrepancia")
        for it in data:
            self.imprime("%s\t%s\t\t%s\t\t%s" % it)
        self.imprime("")
        self.imprime("Discrepancia: %s" % chi_cuadrado)


        ### El grado de libertad: k - r - 1 = 5 - 0 - 1 = 4
        grado_libertad = clases - 0 - 1
        self.imprime("\n=== TABLA CHI-2")
        self.imprime("\tGrados de libertad: %s" % grado_libertad)

        cabecera_cuartiles=[]
        tablaChi = self.cargaTablaChiCuadrado( cabecera_cuartiles, self._chi2_file )
        indiceProbabilidad=self.getCuartil(chi_cuadrado,grado_libertad,tablaChi)

        alfa_superior = chi2_superior = None
        if indiceProbabilidad > 0:
            # Limite superior:
            alfa_superior = cabecera_cuartiles[indiceProbabilidad]
            chi2_superior = tablaChi[ grado_libertad-1 ][indiceProbabilidad]
            self.imprime(u"\tSignificación superior: alfa=%s (chi2= %s)" % (alfa_superior, chi2_superior))

        # Limite inferior
        alfa_inferior = cabecera_cuartiles[indiceProbabilidad+1]
        chi2_inferior = tablaChi[ grado_libertad-1 ][indiceProbabilidad+1]
        self.imprime(u"\tSignificación inferior: alfa=%s (chi2= %s)" % (alfa_inferior, chi2_inferior))

        self.imprime("\n=== RESULTADOS")
        self.imprime(u"\tSignificación %r (chi2=%s)" % (self._significacion, self._chi2_significacion))
        pasa_el_contraste = chi_cuadrado < self._chi2_significacion

        self.imprime("")
        if not pasa_el_contraste:
            self.imprime(u"RECHAZO la hipótesis con un grado de significación de %s" % self._significacion)
        else:
            self.imprime(u"ACEPTO la hipótesis con un grado de significación de %s" % self._significacion)
        if alfa_superior:
            self.imprime(u"Grado de significación mínimo para no rechazar: %s" % (1-float(alfa_superior)))

        return chi_cuadrado, pasa_el_contraste
        #return chi_cuadrado, chi_teorica # Y me devuelves la tupla con el valor calculado y el resultado de si pasa o no el contraste
        #return chi_cuadrado, pasa_el_contraste # Y me devuelves la tupla con el valor calculado y el resultado de si pasa o no el contraste

if __name__=='__main__':
    chi2_file = "./muia/random/test/tablaChiCuadrado.csv"
    from muia.random.mersenne_twister_engine import MersenneTwisterEngine
    generator = MersenneTwisterEngine()
    data = [generator.random() for i in xrange(250000)]

    poker_knuth = PokerKnuth(chi2_file=chi2_file)
    poker_knuth.gestionaPokerKnuth(listaRegistrosNumeros=data)
    exit()

    direccion_fichero = "C:/Users/Jonathan/Google Drive/Master/Metodos de simulacion/practicas/practica 1/poker/ejemplos.txt"
    chi2_file = "C:/Users/Jonathan/Google Drive/Master/Metodos de simulacion/practicas/practica 1/poker/tablaChiCuadrado.csv"

    poker_knuth = PokerKnuth(chi2_file=chi2_file)
    poker_knuth.gestionaPokerKnuth(ficheroRegistrosNumeros=direccion_fichero)


