import pytest
from temperature import isoverheating

def test_high_temperature():
    assert isoverheating(90) is True

def test_normal_temperature():
    assert isoverheating(60) is False

def test_invalid_temperature():
    with pytest.raises(ValueError):
        isoverheating(-5)