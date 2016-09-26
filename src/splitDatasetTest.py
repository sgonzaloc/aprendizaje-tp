import json
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split

ham_txt = json.load(open('dataset_json_test/ham_txt_test.json'))
spam_txt = json.load(open('dataset_json_test/spam_txt_test.json'))

ham_txt_train, ham_txt_test = train_test_split(ham_txt, test_size=0.5, random_state=42)
spam_txt_train, spam_txt_test = train_test_split(spam_txt, test_size=0.5, random_state=42)

with open('dataset_json_test/1/ham_txt_test_1.json', 'w') as outfile:
    json.dump(ham_txt_train, outfile)

with open('dataset_json_test/2/ham_txt_test_2.json', 'w') as outfile:
    json.dump(ham_txt_test, outfile)

with open('dataset_json_test/1/spam_txt_test_1.json', 'w') as outfile:
    json.dump(spam_txt_train, outfile)

with open('dataset_json_test/2/spam_txt_test_2.json', 'w') as outfile:
    json.dump(spam_txt_test, outfile)
