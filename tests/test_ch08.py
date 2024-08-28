import pytest

from pivot_to_python.ch08 import odd

def test_odd() -> None:
    assert odd(1)
    assert not odd(2)
    for e in range(0, 10, 2):
        assert not odd(e)
    for o in range(1, 11, 2):
        assert odd(o)

@pytest.fixture()
def odd_filter():
    def function_to_test(data):
        return filter(odd, data)
    return function_to_test

def test_odd_filter(odd_filter):
    r = list(odd_filter(range(10)))
    assert r == [1, 3, 5, 7, 9]
