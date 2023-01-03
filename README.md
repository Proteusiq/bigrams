# BiGrams

[![PyPI](https://img.shields.io/pypi/v/bigrams?style=flat-square)](https://pypi.python.org/pypi/bigrams/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bigrams?style=flat-square)](https://pypi.python.org/pypi/bigrams/)
[![PyPI - License](https://img.shields.io/pypi/l/bigrams?style=flat-square)](https://pypi.python.org/pypi/bigrams/)
[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)


---

**Documentation**: [https://proteusiq.github.io/bigrams](https://proteusiq.github.io/bigrams)

**Source Code**: [https://github.com/proteusiq/bigrams](https://github.com/proteusiq/bigrams)

**PyPI**: [https://pypi.org/project/bigrams/](https://pypi.org/project/bigrams/)

---

Simply create (N)grams

## Installation

```sh
pip install bigrams
```

## Development

* Clone this repository
* Requirements:
  * [Poetry](https://python-poetry.org/)
  * Python 3.8+
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

### Documentation

The documentation is automatically generated from the content of the [docs directory](./docs) and from the docstrings
 of the public signatures of the source code. The documentation is updated and published as a [Github project page
 ](https://pages.github.com/) automatically as part each release.

### Releasing

Trigger the [Draft release workflow](https://github.com/proteusiq/bigrams/actions/workflows/draft_release.yml)
(press _Run workflow_). This will update the changelog & version and create a GitHub release which is in _Draft_ state.

Find the draft release from the
[GitHub releases](https://github.com/proteusiq/bigrams/releases) and publish it. When
 a release is published, it'll trigger [release](https://github.com/proteusiq/bigrams/blob/master/.github/workflows/release.yml) workflow which creates PyPI
 release and deploys updated documentation.

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

This project was generated using the [wolt-python-package-cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter) template.
