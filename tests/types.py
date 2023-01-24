from dataclasses import dataclass

from bigrams import BigramsType, SentencesType


@dataclass
class Artifacts:
    bigrams: BigramsType
    in_sentences: SentencesType
    out_sentences: SentencesType
