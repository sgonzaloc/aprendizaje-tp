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


# Entrenamiento Reduccion de dimensionalidad
print 'Algoritmo randomforest con PCA'
print 'Entrenamiento PCA'

Cant_Atributos = len(df.columns) - 1
components = int(220)

pca = PCA(n_components=components, copy='False')
start_time = time.time()
pca = pca.fit(X)
print "Tiempo de PCA training ", round(time.time() - start_time,7)
saveClassifier('trained_clasificadores/ClfPCA'+str(components), pca)


# Entrenamiento clasificador
print 'Entrenamiento randomForest con PCA'

_n_trees = 15
_max_features = 110
_max_depth = 110

clf = RandomTrees(_n_trees, _max_features, _max_depth, 1)
X_red = pca.transform(X)
start_time = time.time()
clf = clf.fit(X_red, Y)
print "Tiempo de randomForest con PCA ", round(time.time() - start_time,7)
saveClassifier('trained_clasificadores/ClfRandomForestConPCA'+str(components), clf)
