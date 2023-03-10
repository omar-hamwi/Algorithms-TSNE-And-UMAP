# -*- coding: utf-8 -*-
"""z3_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1geL7b3TVpLmWUdyfTU8Xbpq109NP5ooo
"""

pip install pandas

pip install numpy

pip install sklearn

pip install matplotlib

pip install umap-learn

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib as mpl
import umap
import plotly.express as px

spam = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data")

X = spam.iloc[:,: 57]

distributions = [
    ("Unscaled data", X),
    ("Data after standard scaling", StandardScaler().fit_transform(X)),
    ("Data after min-max scaling", MinMaxScaler().fit_transform(X)),
    ("Data after robust scaling",RobustScaler(quantile_range=(25, 75)).fit_transform(X))
]

distributions_umap = [
    ("Unscaled data", X),
    ("Data after standard scaling", StandardScaler().fit_transform(X)),
    ("Data after min-max scaling", MinMaxScaler().fit_transform(X)),
    ("Data after robust scaling", RobustScaler(quantile_range=(25, 75)).fit_transform(X))
]

title1, X1 = distributions[0]
title2, X2 = distributions[1]
title3, X3 = distributions[2]
title4, X4 = distributions[3]

tsne = TSNE(n_components=2, random_state=0)
projections = tsne.fit_transform(X1)

fig = px.scatter(
    projections, x=0, y=1,
    color=spam.iloc[: , -1], labels={'color': 'spam'}
)
fig.show()

tsne = TSNE(n_components=2, random_state=0)
projections = tsne.fit_transform(X2)

fig = px.scatter(
    projections, x=0, y=1,
    color=spam.iloc[: , -1], labels={'color': 'spam'}
)
fig.show()

tsne = TSNE(n_components=2, random_state=0)
projections = tsne.fit_transform(X3)

fig = px.scatter(
    projections, x=0, y=1,
    color=spam.iloc[: , -1], labels={'color': 'spam'}
)
fig.show()

tsne = TSNE(n_components=2, random_state=0)
projections = tsne.fit_transform(X4)

fig = px.scatter(
    projections, x=0, y=1,
    color=spam.iloc[: , -1], labels={'color': 'spam'}
)
fig.show()

titleU1, XU1 = distributions_umap[0]
titleU2, XU2 = distributions_umap[1]
titleU3, XU3 = distributions_umap[2]
titleU4, XU4 = distributions_umap[3]

projections = umap.UMAP().fit_transform(XU1)

fig = px.scatter(
    projections, x=0, y=1,
    color=spam.iloc[: , -1], labels={'color': 'spam'}
)
fig.show()

projections = umap.UMAP().fit_transform(XU2)

fig = px.scatter(
    projections, x=0, y=1,
    color=spam.iloc[: , -1], labels={'color': 'spam'}
)
fig.show()

projections = umap.UMAP().fit_transform(XU3)

fig = px.scatter(
    projections, x=0, y=1,
    color=spam.iloc[: , -1], labels={'color': 'spam'}
)
fig.show()

projections = umap.UMAP().fit_transform(XU4)

fig = px.scatter(
    projections, x=0, y=1,
    color=spam.iloc[: , -1], labels={'color': 'spam'}
)
fig.show()







































