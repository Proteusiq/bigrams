from dataclasses import dataclass


@dataclass(frozen=True)
class Artifacts:
    bigram_mapper: dict = {
        ("new", "york"): "new_york",
        ("baby", "again!"): "baby_again!",
    }
    in_sentences: list[list[str]] = [
        ["this", "is", "new", "york", "baby", "again!"],
        ["new", "york", "and", "baby", "again!"],
    ]
    out_senteces: list[list[str]] = [
        ["this", "is", "new_york", "baby_again!"],
        ["new_york", "and", "baby_again!"],
    ]
