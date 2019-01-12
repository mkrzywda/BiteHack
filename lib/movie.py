from typing import NamedTuple, List


class Movie(NamedTuple):
    title: str
    year: int
    actors: List[str]
    # rating: float
    keywords: List[str]
    genres: List[str]
    quotes: List[str]
    scenario: List[str]
    direction: List[str]


if __name__ == '__main__':
    movie = Movie(title="ASdas", year=1234, actors=["asd ads"], keywords=["a", "b"], genres=["a", "b"], \
                  quates=["ab", "bc"], scenario = ["a b"], direction=["c d"])
    print(movie)
