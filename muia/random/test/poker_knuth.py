# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'jonathan'
import sys


class PokerKnuth(object):

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
        elif numero >= 0.9 and numero <= 1 : # TODO: ¿numero==1 es un valor válido?
            return 10
        else:
            raise AttributeError("Value %r not in range [0, 1]" % numero)


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

    #def cargaTablaChiCuadrado():
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


    def gestionaPokerKnuth(self, ficheroRegistrosNumeros=None,listaRegistrosNumeros=None):
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
        elif listaRegistrosNumeros != None :
            self.imprime("Calculando el Poker_Knuth a partir de una lista como entrada"," %s ")
            lineas = listaRegistrosNumeros[:]

        numeros = map(float,lineas )
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

        map( self.imprime , frecuenciasObservadas )


        n_iteraciones = 0
        for valor in frecuenciasObservadas:
            n_iteraciones = (n_iteraciones+ valor)

        i_esima_categoria =1
        chi_cuadrado = 0
        frecuenciaEsperadaAux=0

        data = []
        for frecuenciaCategoria in frecuenciasObservadas:
            frecuenciaEsperadaAux=self.calculaFrecuenciaEsperada(n_iteraciones,i_esima_categoria)
            chi_cuadrado = (chi_cuadrado +   ((((frecuenciaCategoria - frecuenciaEsperadaAux)) **2) / frecuenciaEsperadaAux ))

            data.append((i_esima_categoria, frecuenciaEsperadaAux, chi_cuadrado))
            i_esima_categoria = (i_esima_categoria+1)

        self.imprime("")
        self.imprime("Clase\tfreq\tChi")
        for it in data:
            self.imprime("%s\t%s\t%s" % it)
        self.imprime("")

        self.imprime("mi chi cuadrado temporal es")
        self.imprime(chi_cuadrado,"%f")

        ### El grado de libertad: k - r - 1 = 5 - 0 - 1 = 4
        grado_libertad = clases - 0 - 1
        probabilidad = "0.995"

        cabecera_cuartiles=[]
        tablaChi = self.cargaTablaChiCuadrado( cabecera_cuartiles, self._chi2_file )
        #map(imprime,cabecera_cuartiles)
        indice_x1_a = self.getIndiceGradoLibertad(cabecera_cuartiles,probabilidad)
        chi_teorica = tablaChi[grado_libertad-1][indice_x1_a]#los indices inician en 0: grado_libertad-1
        self.imprime("Con un grado de libertad: ",formato =" %s",end="")
        self.imprime(grado_libertad,formato =" %d ")
        self.imprime("Con una probabilidad: ",formato =" %s",end="")
        self.imprime(probabilidad,formato =" %s ")
        self.imprime("mientras que la chi de referencia es ",formato =" %s ",end="")
        self.imprime(chi_teorica,formato =" %s ")

        pasa_el_contraste = (chi_teorica < chi_cuadrado)

        self.imprime( "Si chi_teorica < chi_cuadrado, se acepta o no la hipotesis" )

        if pasa_el_contraste :
            #imprime( "Entonces: %f < %f " % chiss )
            self.imprime( "Entonces: ",formato="%s",end="" )
            self.imprime(float(chi_teorica),formato="%f",end=" " )
            self.imprime( " < ",formato="%s",end="" )
            self.imprime(chi_cuadrado,formato="%f",end="\n" )
            self.imprime("Se acepta la hipotesis!")
        else:
            #imprime( "Entonces: %f >= %f " % chiss )
            self.imprime( "Entonces: ",formato="%s",end="" )
            self.imprime(float(chi_teorica),formato="%f",end=" " )
            self.imprime( " >= ",formato="%s",end="" )
            self.imprime(chi_cuadrado,formato="%f",end="\n" )
            self.imprime("No se acepta la hipotesis!")

        if ficheroRegistrosNumeros != None:
            # Cerramos el fichero.
            infile.close()

        return chi_cuadrado, pasa_el_contraste # Y me devuelves la tupla con el valor calculado y el resultado de si pasa o no el contraste


if __name__=='__main__':
    direccion_fichero = "C:/Users/Jonathan/Google Drive/Master/Metodos de simulacion/practicas/practica 1/poker/ejemplos.txt"
    chi2_file = "C:/Users/Jonathan/Google Drive/Master/Metodos de simulacion/practicas/practica 1/poker/tablaChiCuadrado.csv"

    poker_knuth = PokerKnuth(chi2_file=chi2_file)
    poker_knuth.gestionaPokerKnuth(ficheroRegistrosNumeros=direccion_fichero)


