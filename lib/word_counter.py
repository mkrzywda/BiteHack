from collections import Counter
import re
from nltk.stem import PorterStemmer
import nltk.data
#nltk.download()

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
porter_stemmer = PorterStemmer()


def word_counter(subtitles):
    cnt = Counter(subtitles.split())
    for i in cnt.copy():
        if i[0].islower() and porter_stemmer.stem(i) != i:
            cnt[porter_stemmer.stem(i)] += cnt[i]
    return cnt