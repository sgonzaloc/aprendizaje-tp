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
clasificador = 'KNeighbors'

print 'PCA con ' + clasificador
for component in alpha:
    print 'alpha: ' + str(component)
    res = cross_validation(X, Y, 'PCA', component, clasificador, 3)

clasificador = 'DecisionTree'
print 'PCA con ' + clasificador
for component in alpha:
    print 'alpha: ' + str(component)
    res = cross_validation(X, Y, 'PCA', component, clasificador, 5)