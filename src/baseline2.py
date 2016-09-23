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

ham_txt = json.load(open('dataset_json_train/ham_txt_train.json'))
spam_txt = json.load(open('dataset_json_train/spam_txt_train.json'))

d_emails = pd.DataFrame(ham_txt + spam_txt, columns=['text'])
d_emails['class'] = ['ham' for _ in range(len(ham_txt))]+['spam' for _ in range(len(spam_txt))]
df = features(d_emails)

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


def evaluarRandomizedSearch(n_min, n_max, n_iter):
	# run randomized search
	for i in xrange(1,n_iter):
		param_dist = {"n_neighbors": sp_randint(n_min, n_max)}
		search = RandomizedSearchCV(KNeighborsClassifier(algorithm='ball_tree', n_jobs=3), param_distributions=param_dist, n_iter=5, n_jobs=3)
		search.fit(X, y)
		best_params_st_searchs = sorted(search.grid_scores_, key = lambda x : x[1]/(x[2]*2), reverse = True)[:2]
		n_neighbors = [params['n_neighbors'] for (params, mean_score, scores) in best_searchs]
		n_min = n_neighbors[0]
		n_max = n_neighbors[1]
		if n_min == n_max:
			break
		print "iteracion: ", i
	print "n_min: ", n_min
	print "n_max: ", n_max

	print("Best parameters set found on development set:")
	print()
	print(best_searchs.best_params_)
	print()
	print("Grid scores on development set:")
	print()
	for params, mean_score, scores in best_searchs.grid_scores_:
	    print("%0.3f (+/-%0.03f) for %r"% (mean_score, scores.std()*2, mean_score/(scores.std()*2), params))
	print()

evaluarRandomizedSearch(1, 50, 5)