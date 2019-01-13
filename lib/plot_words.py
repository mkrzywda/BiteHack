import plotly.plotly
import plotly.graph_objs as go
import numpy as np
import os
import glob
import gensim.downloader as api
from sklearn.manifold import TSNE
import normalization
import word_counter


def cluster_analysis(paths, topn=50):
    model = api.load("glove-twitter-50")
    data = []
    vector, labels, names = [], [], []
    
    for path in paths:
        print('Analyzing: ', path)
        x = normalization.normalize_srt(path)
        words = [i for i, _ in word_counter.word_counter(x).most_common(50)]
        print(words)

        for word in words:
            try:
                vector.append(model.wv[word])
                labels.append(word)
                names.append(path)
            except Exception as e:
                print(e)
                print("Not found %s in vector" % word)

    embedded = TSNE(n_components=2,  init='pca').fit_transform(vector)
    x, y = np.hsplit(embedded, 2)
    x = x.reshape(-1)
    y = y.reshape(-1)
    last = 0
    for i in range(len(names)):
        if i+1 == len(names) or names[i] != names[i+1]:
            print(last, i)

            trace = go.Scattergl(
                x=x[last:i],
                y=y[last:i],
                mode='markers',
                # marker=dict(color='#FFBAD2', line=dict(width=1)),
                text=labels[last:i],
                name=names[i]
            )
            last = i+1
            data.append(trace)

    plotly.offline.plot(data, filename='compare_webgl.html')

def get_all_paths():
    paths = []
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    for path in glob.glob(os.path.join(data_dir, '*.srt')):
        paths.append(path)
    return paths


if __name__ == '__main__':
    paths = get_all_paths()[:10]
    cluster_analysis(paths)
