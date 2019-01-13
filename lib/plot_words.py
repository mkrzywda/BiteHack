import plotly.plotly
import plotly.graph_objs as go
import numpy as np
import os
import glob
import gensim.downloader as api
from sklearn.manifold import TSNE


def cluster_analysis(paths):
    model = api.load("glove-twitter-50")
    data = []
    for path in paths:
        x = normalization.normalize_srt(path)
        z = word_counter.word_counter(x)[:50]
        print(z)

        vector, labels = [], []
        for word in words:
            try:
                vector.append(model.wv[word])
                lables.append(word)
            except:
                print("Not found %s in vector" % word)

        embedded = TSNE(n_components=2).fit_transform(vector)
        x, y = np.hsplit(embedded, 2)

        trace = go.Scattergl(
            x=x.reshape(-1),
            y=y.reshape(-1),
            mode='markers',
            # marker=dict(color='#FFBAD2', line=dict(width=1)),
            text=labels
        )

        data.append(trace)

    plotly.offline.plot(data, filename='compare_webgl.html')

def get_all_paths():
    paths = []
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    for path in glob.glob(os.path.join(data_dir, '*.srt')):
        paths.append(path)
    return paths


if __name__ == '__main__':
    paths = get_all_paths()[:5]
    cluster_analysis(paths)
