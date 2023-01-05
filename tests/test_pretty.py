from bigrams import Grams

from .types import Artifacts


def test_repr(artifacts: Artifacts) -> None:

    assert (
        repr(Grams(window_size=2, threshold=2)) == "Grams(window_size=2, threshold=2)"
    )
