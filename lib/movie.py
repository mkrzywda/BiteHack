from typing import NamedTuple, List
import json, os, glob, identify_title, principals
class Movie():
    def __init__(self):
        self.ID = ''
        self.title = ''
        self.year = int()
        self.actors = list()
        # rating: float
        self.keywords = list()
        self.genres = list()
        self.quotes = list()
        self.scenario = list()
        self.direction = list()
        self.filename = ''
        self.linkIMDB = ''
    def __repr__(self):
        return("ID: {0}, Title {1}, Year {2}, Actors: {3}, Keywords: {4}, Genres: {5}, Quotes: {6}, Scenario: {7},\
         Direction: {8}".format(self.ID,self.title,self.year,self.actors,self.keywords,self.genres,self.quotes,\
                                self.scenario,self.direction))

def add_to_file(movie):
    movies_dict = {}
    if os.path.isfile("../data/movies.json") is False:
        movies_dict = {movie.title + '_' + str(movie.year): movie.__dict__}
        with open('../data/movies.json', 'w') as outfile:
            json.dump(movies_dict, outfile)
    else:
        with open('../data/movies.json', 'r') as infile:
            movies_dict = json.load(infile)
            if movie.title + '_' + str(movie.year) not in movies_dict:
                movies_dict.update({movie.title + '_' + str(movie.year): movie.__dict__})
        with open('../data/movies.json', 'w') as outfile:
            json.dump(movies_dict, outfile)

def movie_exist(movie_title):
    if os.path.isfile("../data/movies.json") is False:
        print("File does not exist")
    else:
        with open('../data/movies.json', 'r') as infile:
            movies_dict = json.load(infile)
            if movie_title in movies_dict:
                return True
    return False



def create_json_file():
    for file in os.listdir('../data/'):
        if file.endswith('.srt'):
            movie = Movie()
            movie = identify_title.load_title(file, movie)
            if movie_exist(movie.title) == False:
                print("Movie already exist in .json file")
                continue
            movie = identify_title.search_title_in_base(movie, '../data/title_data.tsv')
            if movie == False:
                print("Problem: "+file)
                continue
            principal = principals.get_principals(movie, '../data/principals_data.tsv')
            movie = principals.set_principals_name(principal,'../data/basic_personal_data.tsv',movie)
            add_to_file(movie)

create_json_file()
#if __name__ == '__main__':
    #movie = Movie(title="ASdas", year=1234, actors=["asd ads"], keywords=["a", "b"], genres=["a", "b"], \
    #             quates=["ab", "bc"], scenario = ["a b"], direction=["c d"])
    #print(movie)
