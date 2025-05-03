import pytest
from minipkg.core import add


def test_add():
    assert add(2, 3) == 5


def test_add_negative_inputs():
    # Both args negative
    with pytest.raises(ValueError):
        add(-2, -3)
    # First arg negative
    with pytest.raises(ValueError):
        add(-1,  5)
    # Second arg negative
    with pytest.raises(ValueError):
        add( 2, -7)
