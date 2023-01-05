from bigrams import replacer

from .types import Artifacts


def test_replacer(artifacts: Artifacts) -> None:

    sentences = [
        replacer(
            sentence=s,
            bigrams_mapper=artifacts.bigram_mapper,
            window_size=2,
        )
        for s in artifacts.in_sentences
    ]

    assert sentences == artifacts.out_senteces
