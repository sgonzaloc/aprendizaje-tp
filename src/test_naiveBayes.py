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
print 'NaiveBayes'
res = cross_validation(X, Y, 'none', 'none', 'NaiveBayes', 'none')
