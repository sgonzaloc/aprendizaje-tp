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

parameters = [arbol, atributo, profundidad, 1]
clf = RandomTrees(_n_trees, _max_features, _max_depth, _min_samples_split)
clf = clf.fit(X, Y)
saveClassifier('trained/Clasificador.pickle', 'w')