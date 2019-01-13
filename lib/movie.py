from typing import NamedTuple, List
import json
import os.path

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
            movies_dict.update({movie.title + '_' + str(movie.year): movie.__dict__})
            print(movies_dict)
        with open('../data/movies.json', 'w') as outfile:
            json.dump(movies_dict, outfile)

#if __name__ == '__main__':
    #movie = Movie(title="ASdas", year=1234, actors=["asd ads"], keywords=["a", "b"], genres=["a", "b"], \
    #             quates=["ab", "bc"], scenario = ["a b"], direction=["c d"])
    #print(movie)
