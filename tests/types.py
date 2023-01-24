from dataclasses import dataclass
from bigrams import Bigrams, Sentences


@dataclass
class Artifacts:
    bigrams: Bigrams
    in_sentences: Sentences
    out_senteces: Sentences