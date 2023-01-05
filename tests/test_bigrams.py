from .types import Artifacts
from bigrams import Grams


def test_grams(artifacts: Artifacts) -> None:

    bi = Grams(window_size=2, threshold=2)
    sentences = bi.fit(X=artifacts.in_sentences).transform(X=artifacts.in_sentences)
    assert sentences == artifacts.out_senteces

    sentences = Grams(window_size=2, threshold=2).fit_transform(X=artifacts.in_sentences)
    assert sentences == artifacts.out_senteces
