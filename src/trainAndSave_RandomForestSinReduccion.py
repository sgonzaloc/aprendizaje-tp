# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 23:55:33 2016

@author: Agus
"""
import pickle
from features import *
from algorithm import *
import time
# No creo q haga falta importar los reductores por separado si se importa algorithms, pero por si acaso
from sklearn.decomposition import PCA

# Calculamos los features
df = features()
#df = pd.concat([df.iloc[:60, :], df.iloc[71910:, :]], ignore_index=True) #Omitir esta línea para la version real

# Preparamos data para clasificar
X = df.iloc[:, 1:].values
Y = df['class']

# Entrenamiento clasificador
print 'Entrenamiento randomForest sin reduccion'

_n_trees = 15
_max_features = 110
_max_depth = 110

clf = RandomTrees(_n_trees, _max_features, _max_depth, 1)
start_time = time.time()
clf.fit(X, Y)
print "Tiempo de randomForest sin reduccion ", round(time.time() - start_time,7)
saveClassifier('trained_clasificadores/ClfRandomForestSinReduccion', clf)

