from cmath import pi
import unittest
from typing import List
from random import randint


def merge_sort(lst: List, reverse=False) -> List:
    """Implement Merge Sort Algorithm"""
    result = lst.copy()

    merge_sort_helper(result, reverse)

    return result

def merge_sort_helper(lst: List, reverse=False):
    # print('lst', lst)
    if len(lst) < 2:
        return

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    # Recursive call on each half
    merge_sort_helper(left, reverse)
    merge_sort_helper(right, reverse)

    # Two iterators for traversing the two halves
    i = 0
    j = 0
    
    # Iterator for the main list
    k = 0
    
    while i < len(left) and j < len(right):
        if not reverse:
            if left[i] <= right[j]:
                # The value from the left half has been used
                lst[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                lst[k] = right[j]
                j += 1
        else:
            if left[i] > right[j]:
                # The value from the left half has been used
                lst[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                lst[k] = right[j]
                j += 1
        # Move to the next slot
        k += 1

    # For all the remaining values
    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        lst[k]=right[j]
        j += 1
        k += 1


class TestMergeSort(unittest.TestCase):
    def test_empty_list(self):
        actual = merge_sort([])
        expected = []
        self.assertEqual(actual, expected)

    def test_len_one_list(self):
        actual = merge_sort([1])
        expected = [1]
        self.assertEqual(actual, expected)

    def test_specified_list(self):
        actual = merge_sort([2,1,3,2,4,3,5,4,6,5,7,6,8,7,9,8])
        expected = [1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9]
        self.assertEqual(actual, expected)

    def test_compare_to_standard(self):
        rndn = [randint(0, 99) for _ in range(100)]
        actual = merge_sort(rndn)
        expected = sorted(rndn)
        self.assertEqual(actual, expected)

    def test_specified_list_reverse(self):
        actual = merge_sort([2,1,3,2,4,3,5,4,6,5,7,6,8,7,9,8], reverse=True)
        expected = [9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1]
        self.assertEqual(actual, expected)
    
    def test_compare_to_standard_reverse(self):
        rndn = [randint(0, 99) for _ in range(100)]
        actual = merge_sort(rndn, reverse=True)
        expected = sorted(rndn, reverse=True)
        self.assertEqual(actual, expected)

    def test_compare_to_standard_n_lists(self):
        n = 100
        for i in range(n):
            rndn = [randint(0, 99) for _ in range(100)]
            actual = merge_sort(rndn)
            expected = sorted(rndn)
            self.assertEqual(actual, expected)

    def test_compare_to_standard_n_lists_reverse(self):
        n = 100
        for i in range(n):
            rndn = [randint(0, 99) for _ in range(100)]
            actual = merge_sort(rndn, reverse=True)
            expected = sorted(rndn, reverse=True)
            self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main(verbosity=2)