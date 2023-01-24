from typing import Generator

import pytest

from bigrams import Grams

from .types import Artifacts


@pytest.fixture()
def artifacts() -> Generator[Artifacts, None, None]:
    yield Artifacts(
        bigrams={
            ("new", "york"),
            ("baby", "again!"),
        },
        in_sentences=[
            ["this", "is", "new", "york", "baby", "again!"],
            ["new", "york", "and", "baby", "again!"],
        ],
        out_sentences=[
            ["this", "is", "new_york", "baby_again!"],
            ["new_york", "and", "baby_again!"],
        ],
    )


@pytest.fixture()
def model() -> Generator[Grams, None, None]:
    yield Grams(window_size=2, threshold=2)
