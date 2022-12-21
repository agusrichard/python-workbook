import pytest
from unittest import mock


def first_func():
    return 42


def second_func():
    return 42


class TestManualMocking:
    @pytest.mark.xfail(strict=True, msg='we want this test to fail')
    def test_manual(self):
        patcher = mock.patch("test_manual_mocking.first_func", return_value=82)
        patcher.start()
        assert first_func() == 42
        assert False
        patcher.stop()

    def test_manual_follow_up(self):
        assert first_func() == 42, "looks like someone leaked state!"
