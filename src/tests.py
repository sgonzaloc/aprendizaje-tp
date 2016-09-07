import json
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split

ham_txt = json.load(open('dataset_json/ham_txt.json'))
ham_txt_test = json.load(open('dataset_json/ham_txt_test.json'))
ham_txt_train = json.load(open('dataset_json/ham_txt_train.json'))

ham_txtS = len(ham_txt)
ham_txt_testS = len(ham_txt_test)
ham_txt_trainS = len(ham_txt_train)

spam_txt = json.load(open('dataset_json/spam_txt.json'))
spam_txt_test = json.load(open('dataset_json/spam_txt_test.json'))
spam_txt_train = json.load(open('dataset_json/spam_txt_train.json'))

spam_txtS = len(spam_txt)
spam_txt_testS = len(spam_txt_test)
spam_txt_trainS = len(spam_txt_train)

print 'Sizes iguales TEST1: ', ham_txtS == ham_txt_testS + ham_txt_trainS

print 'Sizes iguales TEST2: ', spam_txtS == spam_txt_testS + spam_txt_trainS