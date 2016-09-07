import json
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split

ham_txt = json.load(open('dataset_json/ham_txt.json'))
spam_txt = json.load(open('dataset_json/spam_txt.json'))

ham_txt_train, ham_txt_test = train_test_split(ham_txt, test_size=0.2, random_state=42)
spam_txt_train, spam_txt_test = train_test_split(spam_txt, test_size=0.2, random_state=42)

with open('dataset_json_train/ham_txt_train.json', 'w') as outfile:
    json.dump(ham_txt_train, outfile)

with open('dataset_json_test/ham_txt_test.json', 'w') as outfile:
    json.dump(ham_txt_test, outfile)

with open('dataset_json_train/spam_txt_train.json', 'w') as outfile:
    json.dump(spam_txt_train, outfile)

with open('dataset_json_test/spam_txt_test.json', 'w') as outfile:
    json.dump(spam_txt_test, outfile)
