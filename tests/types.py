from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class Artifacts:
    bigram_mapper: Dict[Tuple[str, str], str]
    in_sentences: List[List[str]]
    out_senteces: List[List[str]]
