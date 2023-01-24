from bigrams import replacer

from .types import Artifacts


def test_replacer(artifacts: Artifacts) -> None:

    sentences = [
        replacer(
            sentence=s,
            bigrams=artifacts.bigrams,
            window_size=2,
        )
        for s in artifacts.in_sentences
    ]

    assert [s.split() for s in sentences] == artifacts.out_sentences  # type: ignore
