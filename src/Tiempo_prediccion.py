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


"""
# Entrenamos Reduccion de dimensionalidad
print 'Cargamos PCA'

pca = loadClassifier('trained_clasificadores/Reductor220')
start_time = time.time()
X_red = pca.transform(X)
print "Pca Training ", round(time.time() - start_time,7)


# Entrenamos clasificador
print 'Cargamos randomforest'

clf = loadClassifier('trained_clasificadores/ClasificadorRed220')
start_time = time.time()
y_pred = clf.predict(X_red)
print "Random Tree post PCA ", round(time.time() - start_time,7)

y_true = Y
confusion = confusion_matrix(y_true, y_pred, labels=["ham", "spam"])
print "confusion_matrix: ", confusion
# Verifico que tan bien predijo  
#result.append([i==j for i, j in zip(y_pred, y_test)])
print round(time.time() - start_time,7)
print round(accuracy_score(y_true, y_pred),7)
print round(f1_score(y_true, y_pred, pos_label='spam'),7)
print round(precision_score(y_true, y_pred, pos_label='spam'),7)
print round(recall_score(y_true, y_pred, pos_label='spam'),7)
"""
"""
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

"""