from typing import NamedTuple, List


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

#if __name__ == '__main__':
    #movie = Movie(title="ASdas", year=1234, actors=["asd ads"], keywords=["a", "b"], genres=["a", "b"], \
    #             quates=["ab", "bc"], scenario = ["a b"], direction=["c d"])
    #print(movie)
