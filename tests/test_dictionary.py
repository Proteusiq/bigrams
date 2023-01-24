from bigrams import Grams

from .types import Artifacts


def test_dictionary(model: Grams, artifacts: Artifacts) -> None:

    dictionary = model.fit(X=artifacts.in_sentences).dictionary

    assert set(dictionary.keys()) == {("baby", "again!"), ("new", "york")}
