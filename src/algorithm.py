# coding=utf-8
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
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
