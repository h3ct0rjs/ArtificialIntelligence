import random

class Perceptron:
    def __init__(self,input_number,step_size=0.1):
        self._ins = input_number
        self._w = [random.random() for _ in range(input_number)]
        self._eta = step_size
        
    def predict(self,inputs):
        weighted_average = sum(w*elm for w,elm in zip(self._w,inputs))
        if weighted_average > 0:
            return 1
        return 0

    def train(self,inputs,ex_output):
        output = self.predict(inputs)
        error = ex_output - output
        if error != 0:
            self._w = [w+self._eta*error*x for w,x in zip(self._w,inputs)]
        return error
#!/usr/bin/env python
from perceptron import Perceptron

## Datos de hombres y mujeres
input_data = [[170,56,1], # Mujer de 1.70m y 56kg
              [172,63,0],# Hombre de 1.72m y 63kg
              [160,50,1], # Mujer de 1.60m y 50kg
              [170,63,0], # Hombre de 1.70m y 63kg
              [174,66,0],# Hombre de 1.74m y 66kg
              [158,55,1],# Mujer de 1.58m y 55kg
              [183,80,0],# Hombre de 1.83m y 80kg
              [182,70,0],# Hombre de 1.82m y 70kg
              [165,54,1]]# Mujer de 1.65m y 54kg

## Creamos el perceptron
pr = Perceptron(3,0.1) # Perceptron con 3 entradas
weights = [] # Lista con los pesos
errors = []  # Lista con los errores

## Fase de entrenamiento
for _ in range(100):
    # Vamos a entrenarlo varias veces sobre los mismos datos
    # para que los 'pesos' converjan
    for person in input_data:
        output = person[-1]
        inp = [1] + person[0:-1] # Agregamos un uno por default
        weights.append(pr._w)
        err = pr.train(inp,output)
        errors.append(err)

h = float(raw_input("Introduce tu estatura en centimetros.- "))
w = float(raw_input("Introduce tu peso en kilogramos.- "))

if pr.predict([1,h,w]) == 1: print "Mujer"
else: print "Hombre"

