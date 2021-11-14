import pytest

from core.cal import Cal

@pytest.fixture
def calc_init():
    return Cal()