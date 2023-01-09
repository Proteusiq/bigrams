from __future__ import annotations

from typing import Dict, List, Set, Tuple

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

Sentences = List[List[str]]
Dictionary = Dict[Tuple[str, str], int]
Mapper = Dict[Tuple[str, ...], str]


def replacer(
    sentence: List[str],
    bigrams_mapper: Dict[Tuple[str, str], str],
    window_size: int = 2,
) -> List[str]:
    """
    Helper function, returns a list of tokens with (N)grams connected

    Args:
        sentence (List[str]): sentence in form of tokens with grams
        bigrams_mapper (Dict[Tuple[str, str], str]): a mapper of (t1, t2) => t1_t2
        window_size (int): how many tokens to be considers: default 2

    Returns:
        List[str]: sentence in form of tokens with (N)grams

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
    """
    Grams allows  you to transform a list of tokens into a list of (N)grams tokens

    Arguments:
        threshold: how many times should tokens appears together to be connected as ngrams
        window_size: the N in (N)gram. how many words should be considered. defaults = 2

    **Usage:**

    ```python
    from bigrams import Grams

    in_sentences = [["this", "is", "new", "york", "baby", "again!"],
                 ["new", "york", "and", "baby", "again!"],
                ]
    g = Grams(window_size=2, threshold=2)

    out_sentences = g.fit_transform(in_stences)
    out_sentences
    ```
    """

    def __init__(
        self,
        threshold: int,
        window_size: int = 2,
    ):

        self.window_size = window_size
        self.threshold = threshold

    def __repr__(self) -> str:

        return f"{self.__class__.__name__}(window_size={self.window_size}, threshold={self.threshold})"

    def fit(self, X: Sentences) -> Grams:

        self.__grams = self.__ngrams(sentences=X)
        self.__X_mapper: Mapper = {gram: "_".join(gram) for gram in self.__grams}
        self.fitted_ = True

        return self

    def transform(self, X: Sentences) -> Sentences:

        return self.__replacer(sentences=X)

    def fit_transform(self, X: Sentences) -> Sentences:

        return self.fit(X).transform(X)

    @property
    def ngrams_(self) -> Set[str]:
        if not getattr(self, "fitted_", False):
            raise RuntimeError(f"{self} is not fitted.")

        return {value for value in self.__X_mapper.values()}

    @ngrams_.setter
    def ngrams_(self, grams: Set[str]) -> None:
        if not getattr(self, "fitted_", False):
            raise RuntimeError(f"{self} is not fitted. Cannot add grams.")

        added_grams: Mapper = {tuple(gram.split("_")): gram for gram in grams}
        self.__X_mapper.update(added_grams)

    def add_ngrams(self, grams: Set[str]) -> Grams:
        self.ngrams_ = grams
        return self

    def remove_ngrams(self, grams: Set[str]) -> Grams:
        if not getattr(self, "fitted_", False):
            raise RuntimeError(f"{self} is not fitted. Cannot delete grams.")
        mapper = {
            key: value for key, value in self.__X_mapper.items() if value not in grams
        }

        self.__X_mapper = mapper
        return self

    def __ngrams(self, sentences: Sentences) -> Dictionary:

        wordcount = compose(
            frequencies,
            lambda s: sliding_window(self.window_size, concatv(*s)),
        )
        dictionary: Dictionary = itemfilter(
            lambda m: m[1] >= self.threshold, wordcount(sentences)
        )

        return dictionary

    def __replacer(self, sentences: Sentences) -> Sentences:

        _replacer = partial(
            replacer, bigrams_mapper=self.__X_mapper, window_size=self.window_size
        )

        return [sentence for sentence in map(_replacer, sentences)]
