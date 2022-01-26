from typing import List
from random import randint
from unittest import TestCase, main


def summ(lst: List) -> int:
    if len(lst) == 0:
        return 0

    if len(lst) == 1:
        return lst[0]

    return lst[0] + summ(lst[1:])

def sigma_notation(n: int, start = 0) -> int:
    if n <= start:
        return start
    
    return n + sigma_notation(n-1, start)


class TestSumSigma(TestCase):
    def test_zero_summ(self):
        actual = summ([])
        expected = 0
        self.assertEqual(actual, expected, 'sum of empty list should be 0')

    def test_list_contains_sigma_notation(self):
        actual = summ([0])
        expected = 0
        self.assertEqual(actual, expected, 'sum of list contains 0 should be 0')

    def test_summ_of_random_list(self):
        nums = [randint(0, 9) for _ in range(100)]
        actual = summ(nums)
        expected = sum(nums)
        self.assertEqual(actual, expected, 'implemented function should be the same like built in library')


if __name__ == "__main__":
    main(verbosity=2)
