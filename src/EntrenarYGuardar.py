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

# Entrenamos clasificador
print 'Entrenamos randomforest solo'

_n_trees = 15
_max_features = 110
_max_depth = 110


clf = RandomTrees(_n_trees, _max_features, _max_depth, 1)
start_time = time.time()
clf = clf.fit(X, Y)
print "random tree solo ", round(time.time() - start_time,7)
saveClassifier('trained/ClasificadorSolo.pickle', 'w')


# Entrenamos Reduccion de dimensionalidad
print 'Entrenamos PCA'

Cant_Atributos = len(df.columns) - 1
components = int(Cant_Atributos * 0.1)
pca = PCA(n_components=components, copy='False')
start_time = time.time()
red = pca.fit(X)
print "Pca Training ", round(time.time() - start_time,7)
saveClassifier('trained/Reductor110.pickle', 'w')

# Entrenamos clasificador
print 'Entrenamos randomforest'

_ntrees = 15
_max_features = 110
_max_depth = 110

clf = RandomTrees(_n_trees, _max_features, _max_depth, 1)
X_red = pca.transform(X)
print X_red.shape
start_time = time.time()
clf = clf.fit(X_red, Y)
print "Random Tree post PCA ", round(time.time() - start_time,7)
saveClassifier('trained/ClasificadorRed110.pickle', 'w')

# Entrenamos Reduccion de dimensionalidad
print 'Entrenamos PCA'

components = 44
pca = PCA(n_components=components, copy='False')
start_time = time.time()
red = pca.fit(X)
print "Pca Training ", round(time.time() - start_time,7)
saveClassifier('trained/Reductor44.pickle', 'w')

# Entrenamos clasificador
print 'Entrenamos randomforest'

_ntrees = 15
_max_features = 44
_max_depth = 110

clf = RandomTrees(_n_trees, _max_features, _max_depth, 1)
X_red = pca.transform(X)
start_time = time.time()
clf = clf.fit(X_red, Y)
print "Random Tree post PCA ", round(time.time() - start_time,7)
saveClassifier('trained/ClasificadorRed44.pickle', 'w')
