# -*- coding: utf-8 -*-
"""SciKit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y_WEhBtBcb25EQyTpZ4OAPWGjx44ZTaz
"""

import seaborn as sns

iris=sns.load_dataset('iris')

iris.head()

X_iris=iris.drop('species', axis=1)
X_iris.shape

y_iris=iris['species']
y_iris.shape

import matplotlib.pyplot as plt
import numpy as np

rng=np.random.RandomState(42)

x=10*rng.rand(50)
y=2*x-1+rng.randn(50)
plt.scatter(x,y)

from sklearn.linear_model import LinearRegression

model=LinearRegression(fit_intercept=True)
model

X=x[:,np.newaxis]
X.shape

model.fit(X,y)

model.coef_

model.intercept_

x_fit=np.linspace(-1,11)
x_fit=x_fit[:,np.newaxis]
y_fit=model.predict(x_fit)

plt.scatter(x,y)
plt.plot(x_fit,y_fit)

from sklearn.model_selection import train_test_split

X_egitim, X_test, y_egitim, y_test=train_test_split(X_iris, y_iris, random_state=1)

from sklearn.naive_bayes import GaussianNB

model=GaussianNB()

model.fit(X_egitim, y_egitim)

y_model=model.predict(X_test)

from sklearn.metrics import accuracy_score

accuracy_score(y_test, y_model)

iris.head()

from sklearn.decomposition import PCA

model=PCA(n_components=2)
model.fit(X_iris)
X_2D=model.transform(X_iris)

iris['PCA1']=X_2D[:,0]
iris['PCA2']=X_2D[:,1]

iris.head()

import seaborn as sns

sns.lmplot(x='PCA1', y='PCA2', hue='species', data=iris, fit_reg=False)

from sklearn.mixture import GaussianMixture

model=GaussianMixture(n_components=3, covariance_type='full')

model.fit(X_iris)

y_gmm=model.predict(X_iris)

iris['cluster']=y_gmm

iris.head()

sns.lmplot(x='PCA1', y='PCA2', data=iris, hue='species', col='cluster', fit_reg=False)

from sklearn.datasets import load_digits

digits=load_digits()

digits.images.shape

fig, axes=plt.subplots(10,10, figsize=(8,8),
                     subplot_kw={'xticks':[], 'yticks':[]},
                     gridspec_kw=dict(hspace=0.1, wspace=0.1))
for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap='binary', interpolation='nearest')

X=digits.data
y=digits.target
print(X.shape)
print(y.shape)

from sklearn.manifold import Isomap

iso=Isomap(n_components=2)
iso.fit(digits.data)
data_2=iso.transform(digits.data)
data_2.shape

plt.scatter(data_2[:,0],data_2[:,1],c=digits.target, alpha=0.5, cmap=plt.cm.get_cmap('tab10', 10))
plt.colorbar(label='digit etiket',ticks=range(10))

from sklearn.model_selection import train_test_split
X_egitim, X_test, y_egitim, y_test=train_test_split(X, y, random_state=0)

from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(X_egitim, y_egitim)

y_model=model.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_model)

from sklearn.metrics import confusion_matrix
matris=confusion_matrix(y_test, y_model)
sns.heatmap(matris, square=True, annot=True, cbar=False)
plt.xlabel('Predict Label')
plt.ylabel('Real Label')

