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

clf = loadClassifier('trained_clasificadores/ClasificadorSolo')
start_time = time.time()
clf = clf.predict(X)
print "random tree solo ", round(time.time() - start_time,7)



# Entrenamos Reduccion de dimensionalidad
print 'Entrenamos PCA'

Cant_Atributos = len(df.columns) - 1
components = int(Cant_Atributos * 0.1)
pca = loadClassifier('trained_clasificadores/Reductor110')
start_time = time.time()
X_red = pca.transform(X)
print "Pca Training ", round(time.time() - start_time,7)


# Entrenamos clasificador
print 'Entrenamos randomforest'

clf = loadClassifier('trained_clasificadores/ClasificadorRed110')
start_time = time.time()
clf = clf.predict(X_red)
print "Random Tree post PCA ", round(time.time() - start_time,7)


# Entrenamos Reduccion de dimensionalidad
print 'Entrenamos PCA'

pca = loadClassifier('trained_clasificadores/Reductor44')
start_time = time.time()
X_red = pca.transform(X)
print "Pca Training ", round(time.time() - start_time,7)


# Entrenamos clasificador
print 'Entrenamos randomforest'

clf = loadClassifier('trained_clasificadores/ClasificadorRed44.pickle')
start_time = time.time()
clf = clf.predict(X_red, Y)
print "Random Tree post PCA ", round(time.time() - start_time,7)

