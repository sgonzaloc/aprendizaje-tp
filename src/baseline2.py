# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

import numpy as np
from sklearn.cross_validation import cross_val_score
from features import *
from algorithm import *
from sklearn.metrics import f1_score
from sklearn.metrics import make_scorer
from sklearn.grid_search import GridSearchCV, RandomizedSearchCV
from sklearn.metrics import classification_report
from scipy.stats import randint as sp_randint
from random import shuffle

df = features()

# Preparo data para clasificar
#X = df[['len', 'count_spaces']].values
X = df.iloc[:, 1:].values
y = df['class']

# Elijo mi clasificador.
#clf = DecisionTree()

# Ejecuto el clasificador entrenando con un esquema de cross validation
# de 10 folds.
#f1_scorer = make_scorer(f1_score, pos_label="spam")
#res = cross_val_score(clf, X, y, scoring='accuracy', cv=10)
#print np.mean(res), np.std(res)
# salida: 0.694277777778 0.00518068587861  : catedra
# salida: 0.989361111111 0.00125339046363 : sin 're:'
# salida: 0.989083333333 0.000984446952593 : con 're:'
# salida: 0.989569444444 0.00125838238806 : con subject most common words
# salida: 0.991375 0.00110143354961 : con most common words y multipart


# Set the parameters by cross-validation
#tuned_parameters = [{'n_neighbors': [1, 10, 100, 1000]}]

#f1_scorer = make_scorer(f1_score, pos_label="spam")
#search = GridSearchCV(KNeighborsClassifier(algorithm='ball_tree'), tuned_parameters, cv=5,
#                       scoring='accuracy')


def evaluarRandomizedSearch(n_min, n_max):
	n_max_ant = -1
	n_min_ant = -1
	scores_ant = []
	n_neighbors_range = range(n_min, n_max)
	n_neighbors_processed = []
	while len(n_neighbors_range) > 0:
		shuffle(n_neighbors_range)
		n_neighbors_to_process = n_neighbors_range[:8]
		param_dist = {"n_neighbors": n_neighbors_to_process}
		searchs = GridSearchCV(KNeighborsClassifier(algorithm='ball_tree', n_jobs=2), param_dist, n_jobs=2, scoring='accuracy')
		searchs.fit(X, y)
		scores = scores_ant + [s for s in searchs.grid_scores_]   
		n_neighbors = [params['n_neighbors'] for (params, mean_score, scores) in scores]
		n_neighbors_processed +=  n_neighbors 
		scores_sorted = sorted(scores, key = lambda x : x[1]/(x[2]*2), reverse = True)
		best_scores = scores_sorted[:4]
		n_max = n_neighbors[0]
		n_min = n_neighbors[3]
		if (n_max == n_max_ant) and (n_min == n_min_ant):
			break
		n_max_ant = n_max
		n_min_ant = n_min
		scores_ant = best_scores
		n_neighbors_range = range(n_min, n_max)
		n_neighbors_range = [n for n in n_neighbors_range if n not in n_neighbors_processed]
		print "n_neighbors_range: ", n_neighbors_range
		print "n_max: ", n_max
		print "n_min: ", n_min
		print "best_scores: ", best_scores
	print "n_min: ", n_min
	print "n_max: ", n_max

	print("Best parameters set found on development set:")
	print()
	print(best_scores[0][2])
	print()
	print("Grid scores on development set:")
	print()
	for params, mean_score, scores in best_scores:
	    print("%0.3f (+/-%0.03f) for %r"% (mean_score, scores.std()*2, mean_score/(scores.std()*2), params))
	print()

evaluarRandomizedSearch(1, 20)
