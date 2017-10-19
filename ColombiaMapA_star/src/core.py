# Global Variable
# Index  Medellin Barranquilla Cartagena Monteria  Bogota Neiva Santa
# Marta Armenia Pereira Cali
from src.util import *
from src.core import *
from pprint import pprint 
from time import sleep

gnHash = {}
hnHash = {}
cities = ['Medellin', 'Barranquilla', 'Cartagena', 'Monteria',
          ',''Bogota', 'Neiva', 'SantaMarta', 'Armenia', 'Pereira', 'Cali']
cityindex = [i for i in enumerate(cities)]


def citymenu():
    choices = []
    print("""##########################
#    Lista de Ciudades:  #
##########################
1. Medellin.
2. Barranquilla.
3. Cartagena.
4. Monteria.
5. Bogota.
6. Neiva.
7. Santa Marta.
8. Armenia.
9. Pereira.
10. Cali.
        """ )
    choices.append(
        int(input("{}Seleccione Ciudad Origen:{}$ {} ".format(white, red, reset))))
    choices.append(
        int(input("{}Seleccione Ciudad Destino:{}$ {}".format(white, red, reset))))
    choices = tuple(choices)
    return choices


def options():
    x = citymenu()

    processFiles()


def processFiles():
    with open('data/gn.txt', 'r') as gn:
        for line in gn.readlines()[1:]:
            tmp = line.strip('\n').split(';')
            tmp.remove('')
            nl = []
            for i in tmp[1:]:
                if i is '*':
                    nl.append('x')
                else:
                    nl.append(float(i))
            gnHash[tmp[0]] = list(zip(cities, nl))
    sleep(5)
    Grafo = gnHash  # Representacion del Grafo
    print('\n{}MetaInformacion del Grafo'.format(ok))
    print('\n{}**************************'.format(white))
    print('{}{}INFORMACION  DEL GRAFO {}: '.format(bold, red, reset))
    print('{}**************************'.format(white))
    pprint(Grafo)
    sleep(5)


    with open('data/hn.txt', 'r') as hn:
        for linex in hn.readlines()[1:]:
            tmp = linex.strip('\n').split(';')
            tmp.remove('')
            nl = []
            for i in tmp[1:]:
                if i is '*':
                    nl.append('x')
                else:
                    nl.append(float(i))
            hnHash[tmp[0]] = list(zip(cities, nl))
    #print('\n{}**************************'.format(white))
    #print('{}{}INFORMACION  DE HEURISTICA {}: '.format(bold, red, reset))
    #print('{}**************************'.format(white))
    #pprint(hnHash)  #Pone como en un Json


def astarmethod(Grafo, origen='Medellin', destino='SantaMarta'):

    if origen == destino:
        return
    Abiertos = set()
    Cerrados = set()

    heapmin = []
    abiertos.add(origen)
