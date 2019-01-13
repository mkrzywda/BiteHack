import csv
import re


def search_title_in_base(Movie, base):
    with open(base) as titles:
        titles = csv.reader(titles, delimiter='\t')
        for row in titles:
            mapping = [(':', ''), ('\'', '')]
            for k, v in mapping:
                row[2] = row[2].replace(k, v)
            if Movie.title in row[2] and (row[5] == Movie.year or Movie.year == '') and row[1] == 'movie':
                Movie.ID = row[0]
                Movie.linkIMDB = 'www.imdb.com/title/'+row[0]+'/'
                Movie.genres = list(row[-1].split(','))
                print(Movie.title)
                return Movie
    return False

def load_title(file, Movie):
    Movie.filename = file
    mapping = [('(',' '), (')',' '), ('_',' '), ('.', ' '),(':', ''), ('\'', '')]
    for k, v in mapping:
        file = file.replace(k, v)
    position = re.search("\d\d\d\d",file).start()
    #print(position)
    date = 0
    if position > 0:
        date = file[position:position + 4]
        file = file[:position]
    file = file.rstrip(' ')
    Movie.title = file
    Movie.year = date
    return Movie

#test_movie = movie.Movie()

#test_movie = load_title("The.Avengers.2012.DVDRip.X264.AC3-NYDIC.srt", test_movie)

#print(search_title_in_base(test_movie, '../data/title_data.tsv').ID)
