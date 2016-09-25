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
alpha = [Cant_Atributos * 0.1, Cant_Atributos * 0.2,  Cant_Atributos * 0.3, Cant_Atributos * 0.4, Cant_Atributos * 0.5, Cant_Atributos * 0.6, Cant_Atributos * 0.7]
alpha =  [int(round(component)) for component in alpha]

# Clasificador 1 y sus parametros
clasificador = 'RandomTrees'
parameters =  [15, 0.1, 110, 1]

print 'PCA con ' + clasificador
for component in alpha:
    print 'alpha: ' + str(component)
    res = cross_validation(X, Y, 'PCA', component, clasificador, parameters)

#Clasificador numero 2 y sus parametros
clasificador = 'DecisionTree'
parameters = 110

print 'PCA con ' + clasificador
for component in alpha:
    print 'alpha: ' + str(component)
    res = cross_validation(X, Y, 'PCA', component, clasificador, parameters)