from math import prod
from typing import List
from unittest import TestCase, main


def mult_list(lst: List) -> int:
    if len(lst) == 0:
        return 0

    if len(lst) == 1:
        return lst[0]

    return lst[0] * mult_list(lst[1:])

def mult(n: int, start = 1) -> int:
    if n <= start:
        return start
    
    return n * mult(n-1, start)


class TestMult(TestCase):
    def test_one_mult(self):
        actual = mult(1)
        expected = 1
        self.assertEqual(actual, expected, 'multiplication 1 should be 1')

    def test__mult(self):
        actual = mult(9)
        expected = prod([i for i in range(1, 10)])
        self.assertEqual(actual, expected, 'multiplication 10 should be equal to prod result')


if __name__ == "__main__":
    main(verbosity=2)
