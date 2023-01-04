from __future__ import annotations

from typing import Any, TypeAlias

from cytoolz import (
    compose,
    concatv,
    frequencies,
    itemfilter,
    map,
    partial,
    sliding_window,
)
from more_itertools import replace

Sentences: TypeAlias = list[list[str]]
Dictionary: TypeAlias = dict[tuple[str, str], int]


def replacer(
    sentence: list[str],
    bigrams_mapper: dict[tuple[str, str], str],
    window_size: int,
) -> list[str]:
    # our predict function
    # smart replacer
    # place for improvement

    for key, value in bigrams_mapper.items():
        pred = lambda *args: args == key  # flake8: noqa
        substitutes = [value]

        sentence = [
            t
            for t in replace(
                sentence,
                pred,
                substitutes,
                window_size=window_size,
            )
        ]
    return sentence


class Grams:
    def __init__(
        self,
        window_size: int,
        threshold: int,
    ):

        self.window_size = window_size
        self.threshold = threshold

    def __repr__(self) -> str:
        # pragma: no cover
        return f"{self.__class__.__name__}(window_size={self.window_size}, threshold={self.threshold})"

    def fit(self, X: Sentences) -> Grams:

        X_ = self.__ngrams(X=X)
        self.X_mapper = {gram: "_".join(gram) for gram in X_}

        return self

    def transform(self, X: Sentences) -> Sentences:

        return self.__replacer(Xi=X)

    def __ngram(self, X: Sentences) -> Any:

        return sliding_window(self.window_size, concatv(*X))

    def __clip(self, X: dict[str, int]) -> Any | bool:
        _, v = X
        return v >= self.threshold  # type: ignore

    def __ngrams(self, X: Sentences) -> Any | Dictionary:

        wordcount = compose(frequencies, self.__ngram)
        dictionary = itemfilter(self.__clip, wordcount(X))

        return dictionary

    def __replacer(self, Xi: Sentences) -> Sentences:
        # smart replacer
        # place for improvement

        _replacer = partial(
            replacer, bigrams_mapper=self.X_mapper, window_size=self.window_size
        )
        X_ = map(_replacer, Xi)

        return [x for x in X_]
