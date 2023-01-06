from bigrams import Grams

from .types import Artifacts


def test_ngram(model: Grams, artifacts: Artifacts) -> None:

    ngrams = model.fit(X=artifacts.in_sentences).ngrams_
    assert ngrams == {"baby_again!", "new_york"}


def test_setter(model: Grams, artifacts: Artifacts) -> None:

    model.fit(X=artifacts.in_sentences)
    model.ngrams_ = {"john_doe", "jane_doe"}
    assert model.ngrams_ == {
        "baby_again!",
        "new_york",
        "john_doe",
        "jane_doe",
    }


def test_add_grams(model: Grams, artifacts: Artifacts) -> None:

    model.fit(X=artifacts.in_sentences)
    model.add_ngrams(grams={"john_doe", "jane_doe"})
    assert model.ngrams_ == {
        "baby_again!",
        "new_york",
        "john_doe",
        "jane_doe",
    }


def test_remove_grams(model: Grams, artifacts: Artifacts) -> None:

    model.fit(X=artifacts.in_sentences)
    model.remove_ngrams(grams={"john_doe", "jane_doe"})
    assert model.ngrams_ == {
        "baby_again!",
        "new_york",
    }
