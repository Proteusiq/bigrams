from .types import Artifacts
import pytest




@pytest.fixture()
def artifacts() -> Artifacts:
    yield Artifacts()
