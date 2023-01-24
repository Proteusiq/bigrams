from bigrams import replacer

from .types import Artifacts


def test_replacer(artifacts: Artifacts) -> None:

    sentences = [
        replacer(
            sentence=s,
            bigrams=artifacts.bigrams,
            window_size=2,
        ).split()
        for s in artifacts.in_sentences
    ]

    assert sentences == artifacts.out_sentences
