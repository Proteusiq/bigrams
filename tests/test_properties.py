from bigrams import Grams

from .types import Artifacts


def test_ngram(model: Grams, artifacts: Artifacts) -> None:

    ngrams = model.fit(X=artifacts.in_sentences).ngrams_

    assert ngrams == {("baby", "again!"), ("new", "york")}


def test_setter(model: Grams, artifacts: Artifacts) -> None:

    model.fit(X=artifacts.in_sentences)
    model.ngrams_ = {("john","doe"), ("jane", "doe")}
    assert model.ngrams_ == {
        ("baby", "again!"),
        ("new","york"),
        ("john","doe"),
        ("jane","doe"),
    }


def test_add_grams(model: Grams, artifacts: Artifacts) -> None:

    model.fit(X=artifacts.in_sentences)
    model.add_ngrams(grams={("john","doe"), ("jane", "doe")})
    assert model.ngrams_ == {
        ("baby", "again!"),
        ("new","york"),
        ("john","doe"),
        ("jane","doe"),
    }


def test_remove_grams(model: Grams, artifacts: Artifacts) -> None:

    model.fit(X=artifacts.in_sentences)
    model.remove_ngrams(grams={("john","doe"), ("jane", "doe")})
    assert model.ngrams_ == {
        ("baby", "again!"),
        ("new","york"),
    }
