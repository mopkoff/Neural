import pandas as pd
from sklearn import linear_model
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import numpy as np

df = pd.read_csv('datasets/titanic.csv')

data = np.asarray(df.sample(frac=1), dtype=np.float64)

size = len(df)
test_slice = int(size / 10)

X_train = data[test_slice:, :-1]
y_train = data[test_slice:, -1]

X_test = data[:test_slice, :-1]
y_test = data[:test_slice, -1]

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

