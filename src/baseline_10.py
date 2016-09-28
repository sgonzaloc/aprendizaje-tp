import numpy as np
from sklearn.cross_validation import cross_val_score
from features import *
from algorithm import *

# Calculamos los features
df = features()