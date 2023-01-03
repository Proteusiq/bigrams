from cytoolz import (
    compose,
    frequencies,
    itemfilter,
    partial,
    sliding_window,
    map,
    concatv,
)
from more_itertools import replace


# our predict function
def replacer(sentence, bigrams_mapper: dict[tuple[str, str], str], window_size: int):
    # smart replacer
    # place for improvement

    for key, value in bigrams_mapper.items():
        pred = lambda *args: args == key
        substitutes = [value]

        sentence = [
            t for t in replace(sentence, pred, substitutes, window_size=window_size)
        ]
    return sentence


class Grams:
    def __init__(self, window_size: int, threshold: int) -> "Grams":

        self.window_size = window_size
        self.threshold = threshold

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def fit(self, X):

        X_ = self.__ngrams(X=X)
        self.X_mapper = {gram: "_".join(gram) for gram in X_}

        return self

    def transform(self, X):

        return self.__replacer(Xi=X)

    def __ngram(self, X: list[list[str]]):

        return sliding_window(self.window_size, concatv(*X))

    def __clip(self, X: dict[str, int]):
        _, v = X
        return v >= self.threshold

    def __ngrams(self, X):

        wordcount = compose(
            frequencies, self.__ngram
        )
        dictionary = itemfilter(
            self.__clip, wordcount(X)
        )

        return dictionary

    def __replacer(self, Xi):
        # smart replacer
        # place for improvement

        _replacer = partial(
            replacer, bigrams_mapper=self.X_mapper, window_size=self.window_size
        )
        X_ = map(_replacer, Xi)

        return [x for x in X_]
