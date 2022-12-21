import pytest


@pytest.fixture
def first():
    print("before first function")
    yield 1
    print("after first function")


@pytest.fixture
def second(first):
    print("before second function")
    yield 2
    print("after second function")


def test_first_second(second):
    print("in the real test")

    assert second == 2, "second is supposed to be 2"

