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
    window_size: int = 2,
) -> list[str]:
    """
    Helper function, returns a list of tokens with (N)grams connected

    Args:
        sentence (list[str]): sentence in form of tokens with grams
        bigrams_mapper (dict[tuple[str, str], str]): a mapper of (t1, t2) => t1_t2
        window_size (int): how many tokens to be considers: default 2

    Returns:
        list[str]: sentence in form of tokens with (N)grams

    Usage:

    ```python
    from bigrams import replacer

    bigram_mapper={("new", "york"): "new_york",}
    in_sentence = ["this", "is", "new", "york", "baby", "again!"]
    out_sentence = replacer(sentence=in_setnece,
                            bigrams_mapper=bigrams_mapper,
                            window_size=2,
                    )
    assert out_sentence == ["this", "is", "new_york", "baby", "again!"]
    ```
    """
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

        return f"{self.__class__.__name__}(window_size={self.window_size}, threshold={self.threshold})"

    def fit(self, X: Sentences) -> Grams:

        X_ = self.__ngrams(X=X)
        self.X_mapper = {gram: "_".join(gram) for gram in X_}

        return self

    def transform(self, X: Sentences) -> Sentences:

        return self.__replacer(Xi=X)

    def fit_transform(self, X: Sentences) -> Sentences:

        return self.fit(X).transform(X)

    def __ngrams(self, X: Sentences) -> Any | Dictionary:

        wordcount = compose(
            frequencies,
            lambda s: sliding_window(self.window_size, concatv(*s)),
        )
        dictionary = itemfilter(lambda m: m[1] >= self.threshold, wordcount(X))

        return dictionary

    def __replacer(self, Xi: Sentences) -> Sentences:
        # smart replacer
        # place for improvement

        _replacer = partial(
            replacer, bigrams_mapper=self.X_mapper, window_size=self.window_size
        )
        X_ = map(_replacer, Xi)

        return [x for x in X_]
