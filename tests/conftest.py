from collections.abc import Generator

import pytest

from .types import Artifacts


@pytest.fixture()
def artifacts() -> Generator[Artifacts, None, None]:
    yield Artifacts(
        bigram_mapper={
            ("new", "york"): "new_york",
            ("baby", "again!"): "baby_again!",
        },
        in_sentences=[
            ["this", "is", "new", "york", "baby", "again!"],
            ["new", "york", "and", "baby", "again!"],
        ],
        out_senteces=[
            ["this", "is", "new_york", "baby_again!"],
            ["new_york", "and", "baby_again!"],
        ],
    )
