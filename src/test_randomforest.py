# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

import numpy as np
from features import *
from algorithm import *

# Calculamos los features
df = features()

# Preparamos data para clasificar
X = df.iloc[:, 1:].values
Y = df['class']

# Hacemos cross validation
print 'randomforest'

arboles = [2, 5, 10, 15, 20]
atributos = [None, 'auto', 0.1, 0.5, 0.8]
Cant_Atributos = len(df.columns) -1
Profundidades = [Cant_Atributos * 0.1, Cant_Atributos * 0.5, Cant_Atributos * 0.8]
Profundidades =  [round(Profundidad) for Profundidad in Profundidades]

for arbol in arboles:
    parameters = [arbol, 'sqrt', 'none', 1]
    print 'arboles: ' + str(arbol)
    res = cross_validation(X, Y, 'none', 'none', 'RandomTrees', parameters)

for atributo in atributos:
    parameters = [10, atributo, 'none', 1]
    print 'atributos: ' + str(atributo)
    res = cross_validation(X, Y, 'none', 'none', 'RandomTrees', parameters)

for Profundidad in Profundidades:
    parameters = [10, 'sqrt', Profundidad, 1]
    print 'profundidad: ' + str(profundidad)
    res = cross_validation(X, Y, 'none', 'none', 'RandomTrees', profundidad)