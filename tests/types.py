from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Artifacts:
    bigram_mapper: Dict[Tuple[str, str], str]
    in_sentences: List[List[str]]
    out_senteces: List[List[str]]
