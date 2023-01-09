# (N)Grams
![bigrams](bigrams.png)
> Simply create (N)grams: N ~ Bi | Tri ...

[![PyPI](https://img.shields.io/pypi/v/bigrams?style=flat-square)](https://pypi.python.org/pypi/bigrams/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bigrams?style=flat-square)](https://pypi.python.org/pypi/bigrams/)
[![PyPI - License](https://img.shields.io/pypi/l/bigrams?style=flat-square)](https://pypi.python.org/pypi/bigrams/)
[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)


Welcome to bigrams, a Python project that provides a non-intrusive way to connect tokenized sentences in (N)grams.
This tool is designed to work with tokenized sentences, and it is focused on a single task: providing an efficient way
to merge tokens from a list of tokenized sentences.

It's non-intrusive as it leaves tokenisation, stopwords removal and other text preprocessing out of its flow.

---

**Source Code**: [https://github.com/proteusiq/bigrams](https://github.com/proteusiq/bigrams)

**PyPI**: [https://pypi.org/project/bigrams/](https://pypi.org/project/bigrams/)

---


## Installation

```sh
pip install -U bigrams
```

## Usage

To use bigrams, import it into your Python script, and use `scikit-learn`-ish API to transform your tokens.

```python
from bigrams import Grams

# expects tokenised sentences
in_sentences = [["this", "is", "new", "york", "baby", "again!"],
              ["new", "york", "and", "baby", "again!"],
            ]
g = Grams(window_size=2, threshold=2)

out_sentences = g.fit_transform(in_stences)
print(out_sentences)
# [["this", "is", "new_york", "baby_again!"],
#   ["new_york", "and", "baby_again!"],
#  ]
```

## Development

* Clone this repository
* Requirements:
  * [Poetry](https://python-poetry.org/)
  * Python 3.7+
* Create a virtual environment and install the dependencies

```sh
poetry install
```

* Activate the virtual environment

```sh
poetry shell
```

### Testing

```sh
pytest
```

### Pre-commit

Pre-commit hooks run all the auto-formatters (e.g. `black`, `isort`), linters (e.g. `mypy`, `flake8`), and other quality
 checks to make sure the changeset is in good shape before a commit/push happens.

You can install the hooks with (runs for each commit):

```sh
pre-commit install
```

Or if you want them to run only for each push:

```sh
pre-commit install -t pre-push
```

Or if you want e.g. want to run all checks manually for all files:

```sh
pre-commit run --all-files
```

---

# Contributing are welcome

# ToDo:
 - [ ] ~~create a save & load function~~
 - [ ] compare it with gensim Phrases
 - [ ] write replacer in Rust - [PyO3](https://github.com/PyO3/pyo3)
