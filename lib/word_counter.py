from collections import Counter
import re


def word_counter(s):
    string_string = " ".join(s)
    re_word = re.sub(r'[^\w\s]', '', string_string)
    cnt = Counter(re_word.split())
    return cnt