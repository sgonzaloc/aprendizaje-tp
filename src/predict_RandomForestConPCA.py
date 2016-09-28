# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 23:55:33 2016

@author: Agus
"""
import pickle
from features_test import *
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

# Entrenamos Reduccion de dimensionalidad
print 'Cargamos PCA'
components = int(220)

pca = loadClassifier('trained_clasificadores/ClfPCA'+components)
start_time = time.time()
X_red = pca.transform(X)
print "Tiempo de PCA prediction ", round(time.time() - start_time,7)


# Cargamos clasificador
print 'Cargamos randomforest'
_max_features = 110

clf = loadClassifier('trained_clasificadores/'+_max_features)
start_time = time.time()
y_pred = clf.predict(X_red)
print "Tiempo de randomForest con PCA ", round(time.time() - start_time,7)


# Metricas de prediccion
y_true = Y
confusion = confusion_matrix(y_true, y_pred, labels=["ham", "spam"])
print "confusion_matrix: ", confusion
print "Tiempo de prediccion ", round(time.time() - start_time,7)
print "Accurracy ", round(accuracy_score(y_true, y_pred),7)
print "F1 ", round(f1_score(y_true, y_pred, pos_label='spam'),7)
print "Precision ", round(precision_score(y_true, y_pred, pos_label='spam'),7)
print "Recall ", round(recall_score(y_true, y_pred, pos_label='spam'),7)

