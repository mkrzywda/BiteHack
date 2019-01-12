from collections import Counter
import re
from nltk.stem import PorterStemmer

porter_stemmer = PorterStemmer()


def word_counter(s):
    string_string = " ".join(s).lower()
    re_word = re.sub(r'[^\w\s]', '', string_string)
    cnt = Counter(re_word.split())
    for i in cnt.copy():
        if porter_stemmer.stem(i) != i:
            cnt[porter_stemmer.stem(i)] += cnt[i]
    return cnt
