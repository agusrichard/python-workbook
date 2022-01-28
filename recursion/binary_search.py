from typing import List
from unittest import main, TestCase


def binary_search(lst: List, val: int) -> int:
    if len(lst) == 0:
        return -1

    return binary_search_helper(lst, val, 0, len(lst)-1)

def binary_search_helper(lst: List, val: int, start: int, end: int) -> int:
    if start > end:
        return -1

    mid = (start + end) // 2

    if val == lst[mid]:
        return mid
    elif val < lst[mid]:
        return binary_search_helper(lst, val, start, mid-1)
    else:
        return binary_search_helper(lst, val, mid+1, end)


class TestBinarySearch(TestCase):
    def test_empty_iist(self):
        actual = binary_search([], 0)
        expected = -1
        self.assertEqual(actual, expected)

    def test_specified_list(self):
        nums = [0,1,2,3,4]
        self.assertEqual(binary_search(nums, 0), 0)
        self.assertEqual(binary_search(nums, 1), 1)
        self.assertEqual(binary_search(nums, 2), 2)
        self.assertEqual(binary_search(nums, 3), 3)
        self.assertEqual(binary_search(nums, 4), 4)

    def test_list_all_found(self):
        nums = [i for i in range(100)]
        for i in range(100):
            actual = binary_search(nums, i)
            expected = i
            self.assertEqual(actual, expected)

    def test_list_all_not_found(self):
        nums = [-i for i in range(1, 100)]
        for i in range(100):
            actual = binary_search(nums, i)
            expected = -1
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    main(verbosity=2)