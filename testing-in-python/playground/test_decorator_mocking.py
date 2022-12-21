import pytest
from unittest import mock


def first_func():
    return 42


def second_func():
    return 42


class TestDecoratorMocking(object):
    """This is better, but:
        1. Confusing when we start layering ``pytest`` decorators like
        ``@pytest.mark`` with ``@mock.patch``.
        2. Doesn't work when used with fixtures.
        3. Forces you to accept `mock_fn` as an argument even when the
        mock is just set up and never used in your test - more boilerplate.
    """

    @pytest.mark.xfail(strict=True, msg="We want this test to fail.")
    @mock.patch("test_decorator_mocking.first_func", return_value=84)
    def test_decorator(self, mock_fn):
        assert first_func() == 84
        assert False

    def test_decorator_follow_up(self):
        assert first_func() == 42

    @pytest.fixture
    @mock.patch("playground.test_decorator_mocking.first_func", return_value=84)
    def mock_fn(self, _):
        return

    def test_decorator_with_fixture(self, mock_fn):
        assert first_func() == 84, "@mock and fixtures don't mix!"
