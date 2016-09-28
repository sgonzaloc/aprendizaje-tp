# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 23:55:33 2016

@author: Agus
"""
import pickle
from features_test_1 import *
from algorithm import *
import time
# No creo q haga falta importar los reductores por separado si se importa algorithms, pero por si acaso
from sklearn.decomposition import PCA

# Calculamos los features
df = features_test()
#df = pd.concat([df.iloc[:60, :], df.iloc[71910:, :]], ignore_index=True) #Omitir esta línea para la version real

# Preparamos data para clasificar
X = df.iloc[:, 1:].values
Y = df['class']

# Prediccion clasificador
print 'Algoritmo randomforest sin reduccion'
print 'Prediccion randomforest sin reduccion'

_n_trees = 15
_max_features = 110
_max_depth = 110

clf = loadClassifier('trained_clasificadores/ClfRandomForestSinReduccion')
start_time = time.time()
y_pred = clf.predict(X)
print "Tiempo de randomForest sin reduccion ", round(time.time() - start_time,7)

# Metricas de prediccion
y_true = Y
confusion = confusion_matrix(y_true, y_pred, labels=["ham", "spam"])
print "confusion_matrix: ", confusion
print "Tiempo de prediccion ", round(time.time() - start_time,7)
print "Accurracy ", round(accuracy_score(y_true, y_pred),7)
print "F1 ", round(f1_score(y_true, y_pred, pos_label='spam'),7)
print "Precision ", round(precision_score(y_true, y_pred, pos_label='spam'),7)
print "Recall ", round(recall_score(y_true, y_pred, pos_label='spam'),7)

