from bigrams import Grams

from .types import Artifacts


def test_grams(artifacts: Artifacts) -> None:

    bi = Grams(window_size=2, threshold=2)
    sentences = bi.fit(X=artifacts.in_sentences).transform(X=artifacts.in_sentences)
    assert sentences == artifacts.out_sentences

    sentences = Grams(window_size=2, threshold=2).fit_transform(
        X=artifacts.in_sentences
    )
    assert sentences == artifacts.out_sentences
