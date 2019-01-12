import csv
import re
import movie

def search_title_in_base(Movie, base):
    with open(base) as titles:
        titles = csv.reader(titles, delimiter='\t')
        for row in titles:
            if Movie.title in row and (row[5] == Movie.year or Movie.year == '') and row[1] == 'movie':
                Movie.ID = row[0]
                Movie.genres = row[-1].split(',')
                return Movie
    return False

def load_title(file, Movie):
    mapping = [('(',' '), (')',' '), ('_',' '), ('.', ' ')]
    for k, v in mapping:
        file = file.replace(k, v)
    position = re.search("\d\d\d\d",file).start()
    print(position)
    date = 0
    if position > 0:
        date = file[position:position + 4]
        file = file[:position]
    file = file.rstrip(' ')
    Movie.title = file
    Movie.year = date
    return Movie

test_movie = movie.Movie()

test_movie = load_title("Batman v Superman: Dawn of Justice 2016- Comic-Con Trailer .HD.srt", test_movie)

print(search_title_in_base(test_movie, '../data/title_data.tsv').ID)
