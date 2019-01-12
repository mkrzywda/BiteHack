from collections import Counter
import re
string_list = ["Ania lubi jezyk Python bo Python jest taki super", "Wiedze losia, a moze to sen? Nie jednak to jest Python", "Kot tok kto o o oj"]


cnt = Counter()
string_string = " ".join(string_list)

for word in string_string.split():
    re_word = re.sub(r'[^\w\s]', '', word)

    cnt[re_word] += 1
print(cnt)