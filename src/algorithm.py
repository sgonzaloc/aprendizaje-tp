# coding=utf-8
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import PLSRegression
from sklearn.cross_validation import StratifiedKFold
import numpy as np
from sklearn.metrics import confusion_matrix

############################################################
#####                  Clasificadores                  #####
############################################################

def KNeighbors(n_neighbors):
    return KNeighborsClassifier(n_neighbors=n_neighbors, algorithm='ball_tree')

def DecisionTree(max_depth):
	return DecisionTreeClassifier(max_depth=max_depth)
	
def SVM():
    return SVC(kernel='rbf')
    
def RandomTrees(n_trees):
    return RandomForestClassifier(n_estimators=n_trees, max_features='sqrt', max_depth=None, min_samples_split=1)
    
def NaiveBayes():
    return BernoulliNB()
    
############################################################
#####           Reducción de dimensionalidad           #####
############################################################

def PCA(components, x_train, x_test):
    pca = PCA(n_components=components, copy='False')
    x_train = pca.fit_transform(x_train)
    x_test = pca.transform(x_test)
    return x_train, x_test

def PLS_DA(components, X, Y):
	pls_da = PLSRegression(n_components=components)
	y = map((lambda x: ([1, 0] if x == 'ham' else [0, 1])), Y)
	pls_da.fit(X, y)

############################################################
#####                 cross validation                 #####
############################################################

#devuelve una lista de tuplas (x_train, x_test, y_train, y_test)
def kFold(fold, X, Y):
	folds = StratifiedKFold(Y, n_folds=fold)
	return [(X[train_index], X[test_index], Y[train_index], Y[test_index]) for train_index, test_index in folds]

# Toma el x, el y, el nombre de la funcion a utilizar para reducir (o 'none'), la cantidad de dimensiones finales (o 'none')
# el nombre de la funcion a utilizar para clasificar y el parametro que utiliza la funcion (o 'none')
def cross_validation(X, Y, reduction, components, classifier, parameter): 
	folds = kFold(5, X, Y)

	result = []

	for (x_train, x_test, y_train, y_test) in folds:
		# Reduzco dimensiones
		if reduction == 'PCA':
			x_train, x_test = PCA(components, x_train, x_test)
		elif reduction == 'PLS_DA':
			pass #no esta terminado

		# Elijo el clasificador
		if classifier == 'KNeighbors':
			clf = KNeighbors(parameter)
		elif classifier == 'DecisionTree':
			clf = DecisionTree(parameter)
		elif classifier == 'SVM':
			clf = SVM()
		elif classifier == 'RandomTrees':
			clf = RandomTrees(parameter)
		else:
			clf = NaiveBayes()

		# Entreno el clasificador
		clf = clf.fit(x_train, y_train) 

		y_pred = clf.predict(x_test)
		m = confusion_matrix(y_test.values, y_pred, labels=["ham", "spam"])
		print m
		# Verifico que tan bien predijo  
		#result.append([i==j for i, j in zip(y_pred, y_test)])

	return result