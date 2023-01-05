from dataclasses import dataclass


@dataclass
class Artifacts:
    bigram_mapper: dict[tuple[str,str],str]
    in_sentences: list[list[str]]
    out_senteces: list[list[str]]
