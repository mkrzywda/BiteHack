import csv
import re
from movie import Movie

def search_title_in_base(title, base):
    result = []
    with open(base) as titles:
        titles = csv.reader(titles, delimiter='\t')
        for row in titles:
            if title[0] in row and (row[5] == title[1] or title[1] == '') and row[1] == 'movie':
                result.append(row[0])
    return result

def load_title(file):
    mapping = [('(',' '), (')',' '), ('_',' '), ('.', ' ')]
    for k, v in mapping:
        file = file.replace(k, v)
    position = re.search("\d\d\d\d",file).start()
    date = 0
    if position > 0:
        date = file[position:position + 4]
        file = file[:position]
    file = file.rstrip(' ')
    return [file, date]

test_file = load_title("Shrek (2001) DVDRiP KvCD Hockney(TUS Release).en")

print(search_title_in_base(test_file, 'title_data.tsv'))
