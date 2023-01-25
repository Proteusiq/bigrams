from typing import List, Tuple

import pytest

from bigrams import no_repeat

TEST_EXAMPLES = [
    (
        [
            "This",
            "is",
            "is",
            "Jane",
            "Jane_Doe",
            "Doe",
            "whose",
            "cat",
            "cat_is",
            "home",
            "home",
        ],
        "This is Jane_Doe whose cat_is home",
    ),
    (
        [
            "This",
            "was_Jane",
            "Jane_Doe",
            "Doe",
            "whose",
            "cat",
            "cat_is",
            "home",
        ],
        "This was_Jane Jane_Doe whose cat_is home",
    ),
    (
        [
            "This",
            "is",
            "Jane_Doe",
            "Doe",
            "whose",
            "cat",
            "cat",
            "is",
            "home",
        ],
        "This is Jane_Doe whose cat is home",
    ),
]


@pytest.mark.parametrize(
    "example", TEST_EXAMPLES, ids=["word_grams", "grams_word", "word_word"]
)
def test_repeats(example: Tuple[List[str], str]) -> None:

    before_function, after_expected = example

    after_function = no_repeat(before_function)

    assert after_function == after_expected
