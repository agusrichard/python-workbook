import pytest
from unittest import mock


def first_func():
    return 42


def second_func():
    return 42


class TestMockerFixture(object):
    """This is best; the mocker fixture reduces boilerplate and
    stays out of the declarative pytest syntax.
    """

    @pytest.mark.xfail(strict=True, msg="We want this test to fail.")
    def test_mocker(self, mocker):
        mocker.patch("playground.test_mocker_fixture.first_func", return_value=84)
        assert first_func() == 84
        assert False

    def test_mocker_follow_up(self):
        assert first_func() == 42

    @pytest.fixture
    def mock_fn(self, mocker):
        return mocker.patch("playground.test_mocker_fixture.test_basic.first_func", return_value=84)

    def test_mocker_with_fixture(self, mock_fn):
        assert first_func() == 84