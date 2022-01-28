from typing import List
from unittest import TestCase, main


def linear_search(lst: List, val: int) -> int:
    return linear_search_helper(lst, val, 0)


def linear_search_helper(lst: List, val: int, acc: int) -> int:
    if len(lst) == 0:
        return -1

    if lst[0] == val:
        return acc

    return linear_search_helper(lst[1:], val, acc+1)

class TestLinearSearch(TestCase):
    def test_empty_iist(self):
        actual = linear_search([], 0)
        expected = -1
        self.assertEqual(actual, expected)

    def test_specified_list(self):
        nums = [0,1,2,3,4]
        self.assertEqual(linear_search(nums, 0), 0)
        self.assertEqual(linear_search(nums, 1), 1)
        self.assertEqual(linear_search(nums, 2), 2)
        self.assertEqual(linear_search(nums, 3), 3)
        self.assertEqual(linear_search(nums, 4), 4)

    def test_list_all_found(self):
        nums = [i for i in range(100)]
        for i in range(100):
            actual = linear_search(nums, i)
            expected = i
            self.assertEqual(actual, expected)

    def test_list_all_not_found(self):
        nums = [-i for i in range(1, 100)]
        for i in range(100):
            actual = linear_search(nums, i)
            expected = -1
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    main(verbosity=2)
