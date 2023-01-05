from dataclasses import dataclass
import pytest


@dataclass(frozen=True)
class Artifacts:
    bigram_mapper = {
        ("new", "york"): "new_york",
        ("baby", "again!"): "baby_again!",
    }
    in_sentences = [
        ["this", "is", "new", "york", "baby", "again!"],
        ["new", "york", "and", "baby", "again!"],
    ]
    out_senteces = [
        ["this", "is", "new_york", "baby_again!"],
        ["new_york", "and", "baby_again!"],
    ]


@pytest.fixture()
def artifacts():
    yield Artifacts()
