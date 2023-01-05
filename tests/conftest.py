from collections.abc import Generator

import pytest

from .types import Artifacts


@pytest.fixture()
def artifacts() -> Generator[Artifacts, None, None]:
    yield Artifacts()
