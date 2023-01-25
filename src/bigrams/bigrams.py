from __future__ import annotations

import re
from typing import Callable, Dict, Final, List, Set, Tuple

from cytoolz import (
    compose,
    concatv,
    frequencies,
    itemfilter,
    map,
    mapcat,
    partial,
    sliding_window,
)

SentenceType = List[str]
SentencesType = List[SentenceType]
DictionaryType = Dict[Tuple[str, str], int]
BigramsType = Set[Tuple[str, str]]


__FORWARD_REPETITIONS: Final = re.compile(r"[^_](\w+)\s+(\1_\w+)\s+")
__BACKWARD_REPETITIONS: Final = re.compile(r"[_](\w+)\s+(\1[\s+])")
__MIDDLE_REPETITIONS: Final = re.compile(r"\s+(\w+)\s+\1[_]")
__FINAL_REPETITIONS: Final = re.compile(r"\s+(\w+)\s+\1")


def no_repeat(sentence: SentenceType) -> str:
    """
    Removes repeating words in a sentence after merge.

    Args:
    sentence (SentenceType): The sentence to process.

    Returns:
    str: The sentence without repeating words.

    Note:
    The function uses the regular expressions in the variables
    __X_REPETITIONS
    e.g. ["Jane", "Jane_Doe", "is", "home", "home"] => "Jane_Doe is home"

    Usage:
    ```python
    from bigrams import no_repeat

    sentence = ["Jane", "Jane_Doe", "is", "home", "home"]
    sentence_ = no_repeat(sentence)
    assert sentence_ == "Jane_Doe is home"
    """

    sentence_ = " ".join(sentence)
    sentence_ = __FORWARD_REPETITIONS.sub(r" \2 ", sentence_)
    sentence_ = __BACKWARD_REPETITIONS.sub(r"_\2", sentence_)
    sentence_ = __MIDDLE_REPETITIONS.sub(r" \1_", sentence_)
    return __FINAL_REPETITIONS.sub(r" \1", sentence_)


def replacer(
    sentence: SentenceType,
    bigrams: BigramsType,
    window_size: int = 2,
) -> SentenceType:
    """
    Helper function, returns a list of tokens with (N)grams connected

    Args:
        sentence : sentence in form of tokens with grams
        bigrams : a mapper of (t1, t2) => t1_t2
        window_size : how many tokens to be considers: default 2

    Returns:
        sentence : sentence in form of tokens with (N)grams

    Usage:

    ```python
    from bigrams import replacer

    bigrams = {("new", "york")}
    in_sentence = ["this", "is", "new", "york", "baby", "again!"]
    out_sentence = replacer(sentence=in_sentence,
                            bigrams=bigrams,
                            window_size=2,
                    )
    assert out_sentence == ["this", "is", "new_york", "baby", "again!"]
    ```
    """

    sentence_fn: Callable[..., SentenceType] = compose(
        no_repeat,
        lambda d: mapcat(
            (lambda seq: ("_".join(seq),) if seq in bigrams else seq),
            sliding_window(window_size, sentence),
        ),
    )
    return sentence_fn(sentence)


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
        self._dictionary: DictionaryType = {}
        self.window_size = window_size
        self.threshold = threshold

    def __repr__(self) -> str:

        return f"{self.__class__.__name__}(window_size={self.window_size}, threshold={self.threshold})"

    def fit(self, X: SentencesType) -> Grams:

        self.__ngrams(sentences=X)
        self.fitted_ = True

        return self

    def transform(self, X: SentencesType) -> SentencesType:

        return self.__replacer(sentences=X)

    def fit_transform(self, X: SentencesType) -> SentencesType:

        return self.fit(X).transform(X)

    @property
    def dictionary(self) -> DictionaryType:
        return self._dictionary

    @dictionary.setter
    def dictionary(self, _: Set[Tuple[str, str]]) -> None:
        raise AttributeError(f"{self} dictionary cannot be override!")

    @property
    def ngrams_(self) -> Set[Tuple[str, str]]:
        if not getattr(self, "fitted_", False):
            raise RuntimeError(f"{self} is not fitted.")

        return {gram for gram in self._dictionary.keys()}

    @ngrams_.setter
    def ngrams_(self, grams: Set[Tuple[str, str]]) -> None:
        if not getattr(self, "fitted_", False):
            raise RuntimeError(f"{self} is not fitted. Cannot add grams.")

        d: DictionaryType = {gram: self.threshold for gram in grams}
        self._dictionary.update(d)

    def add_ngrams(self, grams: Set[Tuple[str, str]]) -> Grams:
        self.ngrams_ = grams
        return self

    def remove_ngrams(self, grams: Set[Tuple[str, str]]) -> Grams:
        if not getattr(self, "fitted_", False):
            raise RuntimeError(f"{self} is not fitted. Cannot delete grams.")
        mapper = {
            key: value for key, value in self._dictionary.items() if key not in grams
        }

        self._dictionary = mapper

        return self

    def __ngrams(self, sentences: SentencesType) -> DictionaryType:

        wordcount = compose(
            frequencies,
            lambda s: sliding_window(self.window_size, concatv(*s)),
        )
        dictionary: DictionaryType = itemfilter(
            lambda m: m[1] >= self.threshold, wordcount(sentences)
        )

        self._dictionary = dictionary

        return self._dictionary

    def __replacer(self, sentences: SentencesType) -> SentencesType:

        _replacer = partial(
            replacer, bigrams=self.ngrams_, window_size=self.window_size
        )

        return [sentence.split() for sentence in map(_replacer, sentences)]
