import pytest

from bigrams import Grams


def test_get_grams(model: Grams) -> None:
    with pytest.raises(RuntimeError) as e:
        _ = model.ngrams_
    msg, *_ = e.value.args
    assert msg == f"{model} is not fitted."


def test_set_grams(model: Grams) -> None:
    with pytest.raises(RuntimeError) as e:
        model.ngrams_ = {
            ("john", "doe"),
        }
    msg, *_ = e.value.args
    assert msg == f"{model} is not fitted. Cannot add grams."


def test_add_grams(model: Grams) -> None:
    with pytest.raises(RuntimeError) as e:
        model.add_ngrams(
            {
                ("john", "doe"),
            }
        )
    msg, *_ = e.value.args
    assert msg == f"{model} is not fitted. Cannot add grams."


def test_remove_grams(model: Grams) -> None:
    with pytest.raises(RuntimeError) as e:
        model.remove_ngrams(
            {
                ("john", "doe"),
            }
        )
    msg, *_ = e.value.args
    assert msg == f"{model} is not fitted. Cannot delete grams."


def test_add_dictionary(model: Grams) -> None:
    with pytest.raises(AttributeError) as e:
        model.dictionary = {("jane", "doe"): 15}

    msg, *_ = e.value.args
    assert msg == f"{model} dictionary cannot be override!"
