from collections import Counter
import re


def word_counter(s):
    cnt = Counter()
    string_string = " ".join(s)
    for word in string_string.split():
        re_word = re.sub(r'[^\w\s]', '', word)
        cnt[re_word] += 1
    return cnt
