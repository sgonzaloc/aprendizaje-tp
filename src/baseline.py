# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

import numpy as np
from sklearn.cross_validation import cross_val_score
from features import *
from algorithm import *

ham_txt = json.load(open('dataset_json_train/ham_txt_train.json'))
spam_txt = json.load(open('dataset_json_train/spam_txt_train.json'))

d_emails = pd.DataFrame(ham_txt + spam_txt, columns=['text'])
d_emails['class'] = ['ham' for _ in range(len(ham_txt))]+['spam' for _ in range(len(spam_txt))]

# Calculamos los features
df = features(d_emails)

# Preparamos data para clasificar
X = df.iloc[:, 1:].values
Y = df['class']

# Hacemos cross validation
res = cross_validation(X, Y, 'none', 'none', 'SVM', 'none')


# Ejecuto el clasificador entrenando con un esquema de cross validation
# de 10 folds.
#res = cross_val_score(clf, X, y, cv=10)
#print np.mean(res), np.std(res)
#print res 
# salida: 0.694277777778 0.00518068587861  : catedra
# salida: 0.989361111111 0.00125339046363 : sin 're:'
# salida: 0.989083333333 0.000984446952593 : con 're:'
# salida: 0.989569444444 0.00125838238806 : con subject most common words
# salida: 0.991375 0.00110143354961 : con most common words y multipart
