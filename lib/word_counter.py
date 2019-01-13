from collections import Counter
from nltk.stem import PorterStemmer
import nltk.data
import nltk
from nltk.corpus import stopwords
#nltk.download()

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
porter_stemmer = PorterStemmer()
STOPWORDS = set(stopwords.words('english'))
STOPWORDS.add('I')
for i in set(stopwords.words('english')):
    STOPWORDS.add(porter_stemmer.stem(i))


def word_counter(subtitles):
    cnt = Counter(subtitles.split())
    for i in cnt.copy():
        if i[0].islower() and porter_stemmer.stem(i) != i:
            cnt[porter_stemmer.stem(i)] += cnt[i]

    for i in STOPWORDS:
        del cnt[i]
    print(cnt.keys())
    return cnt
