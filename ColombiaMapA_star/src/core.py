#Global Variable
#Index  Medellin Barranquilla Cartagena Monteria  Bogota Neiva Santa Marta Armenia Pereira Cali 
gnHash = {}
hnHash = {}
cities = ['Medellin','Barranquilla','Cartagena','Monteria',',''Bogota','Neiva','Santa','Marta','Armenia','Pereira','Cali']
cityindex =[i for i in enumerate(cities)]


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
    choices.append(int(input("Seleccione Ciudad Origen:>> ")))
    choices.append(int(input("Seleccione Ciudad Destino:>> ")))
    choices = tuple(choices)
    return choices

def options():
    x = citymenu()
    processFiles()
    Graph = Grafo()


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
            gnHash[tmp[0]] = nl

    print('***********Hash***********')
    print('Costo de Camino: ')
    print('**************************')
    print(gnHash)

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
            hnHash[tmp[0]] = nl
    print('\n***********Hash***********')
    print('Valor Heuristico:           ')
    print('**************************')
    print(hnHash)

class Nodo(object):
    def __init__(self, pos=[0, 0], padre=None):
        self.pos = pos
        self.padre = padre
        self.h = distancia(self.pos, pos_f)
 
        if self.padre == None:
            self.g = 0
        else:
            self.g = self.padre.g + 1
        self.f = self.g + self.h



class Graph(object):

    def __init__(self):
        self.nodes = []

    def add(self, node):
        self.nodes.append(node)

    def astar(self, start, end, heuristic=None):
        pass


def num_to_city(number):
    number = str(number)
    switcher = {
        '1': "Medellin",
        '2': 'Barranquilla',
        '3': 'Cartagena',
        '4': 'Monteria',
        '5': 'Bogota',
        '6': 'Neiva',
        '7': 'Santa Marta',
        '8': 'Armenia',
        '9': 'Pereira',
        '10': 'Cali'
    }
    return switcher.get(number, "Wrong index")
