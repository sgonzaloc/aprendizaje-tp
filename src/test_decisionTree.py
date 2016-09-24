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
print 'decisiontree'

Cant_Atributos = len(df.columns) - 1
Profundidades = [Cant_Atributos * 0.1, Cant_Atributos * 0.3,  Cant_Atributos * 0.5, Cant_Atributos * 0.7, Cant_Atributos * 0.9]
Profundidades =  [round(Profundidad) for Profundidad in Profundidades]

for profundidad in Profundidades:
    print 'profundidad: ' + str(profundidad)
    res = cross_validation(X, Y, 'none', 'none', 'DecisionTree', profundidad)
