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
import time
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
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

	times = []
	accuracy = []
	f1 = []
	precision = []
	recall = []
	for (x_train, x_test, y_train, y_test) in folds:
		start_time = time.time()
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
		y_true = y_test.values
		confusion = confusion_matrix(y_true, y_pred, labels=["ham", "spam"])
		print "confusion_matrix: ", confusion
		# Verifico que tan bien predijo  
		#result.append([i==j for i, j in zip(y_pred, y_test)])
		times.append(round(time.time() - start_time,7))
		accuracy.append(round(accuracy_score(y_true, y_pred),7))
		f1.append(round(f1_score(y_true, y_pred, pos_label='spam'),7))
		precision.append(round(precision_score(y_true, y_pred, pos_label='spam'),7))
		recall.append(round(recall_score(y_true, y_pred, pos_label='spam'),7))

	print "tiempo de", classifier, ":", np.mean(times)
	print "accuracy_score :", np.mean(accuracy), np.std(accuracy)
	print "f1_score :", np.mean(f1), np.std(f1)
	print "precision :", np.mean(precision), np.std(precision)
	print "recall_score :", np.mean(recall), np.std(recall)
	return 1