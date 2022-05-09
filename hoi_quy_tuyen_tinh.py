from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from matplotlib import rcParams
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
import statsmodels.api as sm

from sklearn.model_selection import train_test_split

import seaborn as sns
sns.set_style("whitegrid")
sns.set_context("poster")

# special matplotlib argument for improved plots

# import du lieu boston housing

# luu du lieu trong bien boston
boston = load_boston()

# tra ve hinh dang cua mang data
print(boston.data.shape)
# tra ve ten 13 cot
print(boston.feature_names)

# convert du lieu ve dang pasdas
bos = pd.DataFrame(boston.data)

bos['PRICE'] = boston.target

# X gia tri du bao
X = bos.drop('PRICE', axis=1)
# Y gia tri dich
Y = bos['PRICE']
# chia du lieu train_ test
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.33, random_state=5)
print(X_train.shape)  # ti le 66.66% train
print(X_test.shape)  # 33.33 test
print(Y_train.shape)
print(Y_test.shape)

# chay hoi quy tuyen tinh
# import thu vien

# tao doi tuong lm
lm = LinearRegression()
lm.fit(X_train, Y_train)

# cac gia tri du doan luu trong Y_pred
Y_pred = lm.predict(X_test)

# ve bieu do scatter
plt.scatter(Y_test, Y_pred)

# ten truc X
plt.xlabel("Prices: $Y_i$")
# ten truc Y
plt.ylabel("Predicted prices: $\hat{Y}_i$")
# tieu de
plt.title("Prices vs Predicted prices: $Y_i$ vs $\hat{Y}_i$")

# hien thi bieu do
plt.show()

# kiem tra muc do loi cua mot mo hinh dung
# Mean Squared

mse = sklearn.metrics.mean_squared_error(Y_test, Y_pred)
print(mse)
