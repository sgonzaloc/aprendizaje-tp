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
Cant_Atributos = len(df.columns) - 1
alpha = [Cant_Atributos * 0.1, Cant_Atributos * 0.3, Cant_Atributos * 0.5, Cant_Atributos * 0.7, Cant_Atributos * 0.9]
alpha =  [int(round(component)) for component in alpha]
clasificador = 'KNeighbors'

print 'LSA con ' + clasificador
for component in alpha:
    print 'alpha: ' + str(component)
    res = cross_validation(X, Y, 'LSA', component, clasificador, 3)

clasificador = 'DecisionTree'
print 'LSA con ' + clasificador
for component in alpha:
    print 'alpha: ' + str(component)
    res = cross_validation(X, Y, 'LSA', component, clasificador, 5)