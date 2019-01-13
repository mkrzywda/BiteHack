import plotly.plotly
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec
import gensim.downloader as api
from sklearn.manifold import TSNE


def cluster_analysis(words):
    model = api.load("glove-twitter-50")
    vector = []
    lables = []
    for word in words:
        try:
            vector.append(model.wv[word])
            lables.append(word)
        except:
            print("Not found %s in vector" % word)

    # pts = [np.random.random(20) for _ in range(100)]
    # X = np.array(pts)
    X = vector
    X_embedded = TSNE(n_components=2).fit_transform(X)
    x, y = np.hsplit(X_embedded, 2)
    x = x.reshape(-1)
    y = y.reshape(-1)
    trace = go.Scattergl(
        x=x,
        y=y,
        mode='markers',
        marker=dict(color='#FFBAD2', line=dict(width=1)),
        text=lables
    )
    data = [trace]
    plotly.offline.plot(data, filename='compare_webgl.html')
