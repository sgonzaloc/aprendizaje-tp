# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 23:55:33 2016

@author: Agus
"""
import pickle
from features_test_competencia import *
from algorithm import *
import time
# No creo q haga falta importar los reductores por separado si se importa algorithms, pero por si acaso
from sklearn.decomposition import PCA

# Calculamos los features
df = features_test()
#df = pd.concat([df.iloc[:60, :], df.iloc[71910:, :]], ignore_index=True) #Omitir esta línea para la version real

# Preparamos data para clasificar
X = df.values

# Prediccion clasificador

_n_trees = 15
_max_features = 110
_max_depth = 110

clf = loadClassifier('trained_clasificadores/ClfRandomForestSinReduccion')
y_pred = clf.predict(X)

for m in y_pred:
	print m