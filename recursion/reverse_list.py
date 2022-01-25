import random
from typing import List
from unittest import TestCase, main

def reverse_list(x: List):
    if len(x) == 0:
        return []

    if len(x) == 1:
        return [x[0]]

    return reverse_list(x[1:]) + [x[0]]


class TestReverseList(TestCase):
    def test_empty_list(self):
        actual = reverse_list([])
        expected = []
        self.assertEqual(actual, expected)

    def test_single_element(self):
        actual = reverse_list([0])
        expected = [0]
        self.assertEqual(actual, expected)

    def test_5_elements(self):
        actual = reverse_list([0,1,2,3,4])
        expected = [4,3,2,1,0]
        self.assertEqual(actual, expected)

    def test_random_list(self):
        nums = [random.randint(0, 9) for _ in range(10)]
        actual = reverse_list(nums)
        expected = nums[::-1]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    main(verbosity=2)