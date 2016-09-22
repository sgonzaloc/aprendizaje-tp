# coding=utf-8
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.decomposition import PCA


############################################################
#####                  Clasificadores                  #####
############################################################


def KNeighbors(n_neighbors):
    return KNeighborsClassifier(n_neighbors=n_neighbors, algorithm='ball_tree')


def DecisionTree():
    return DecisionTreeClassifier()


def SVM():
    return SVC(kernel='rbf')

def RandomTrees(n_trees, max_features='sqrt', max_depth=None, min_samples_split=1):
    return RandomForestClassifier(n_estimators=n_trees, max_features=max_features, max_depth=max_depth, min_samples_split=min_samples_split)

def NaiveBayes():
    return BernoulliNB()

############################################################
#####           Reducción de dimensionalidad           #####
############################################################

def PCA(components, X, Y):
    pca = PCA(n_components=components, copy='False')
    x = pca.fit_transform(X)
    y = pca.transform(Y)
    return x, y


def PLS_DA():
    pass
