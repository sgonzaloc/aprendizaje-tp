# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 23:55:33 2016

@author: Agus
"""
import pickle
from features import *
from algorithm import *
# No creo q haga falta importar los reductores por separado si se importa algorithms, pero por si acaso
from sklearn.decomposition import PCA

# Calculamos los features
df = features()
df = pd.concat([df.iloc[:30, :], df.iloc[71970:, :]], ignore_index=True) #Omitir esta línea para la version real

# Preparamos data para clasificar
X = df.iloc[:, 1:].values
Y = df['class']

# Entrenamos clasificador
print 'Entrenamos randomforest solo'

_n_trees = 15
_max_features = 0.1
_max_depth = 110

clf = RandomTrees(_n_trees, _max_features, _max_depth, 1)
clf = clf.fit(X, Y)
saveClassifier('trained/ClasificadorSolo.pickle', 'w')

# Entrenamos Reduccion de dimensionalidad
print 'Entrenamos PCA'

Cant_Atributos = len(df.columns) - 1
components = Cant_Atributos * 0.1
pca = PCA(n_components=components, copy='False')
red = pca.fit(X)
saveClassifier('trained/Reductor.pickle', 'w')

# Entrenamos clasificador
print 'Entrenamos randomforest'

arbol = 15
atributo = 0.1
profundidad = 110

clf = RandomTrees(_n_trees, _max_features, _max_depth, 1)
X_red = pca.transform(X)
clf = clf.fit(X_red, Y)
saveClassifier('trained/ClasificadorRed.pickle', 'w')