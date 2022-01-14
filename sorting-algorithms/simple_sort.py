import unittest
from typing import List
from random import randint


def simple_sort(lst: List, reverse=False) -> List:
    """Implement Simple Sort Algorithm"""
    result = lst.copy()

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if reverse:
                if result[j] > result[i]:
                    result[i], result[j] = result[j], result[i]
            else:
                if result[j] < result[i]:
                    result[i], result[j] = result[j], result[i]

    return result

class TestSimpleSort(unittest.TestCase):
    def test_empty_list(self):
        actual = simple_sort([])
        expected = []
        self.assertEqual(actual, expected)

    def test_len_one_list(self):
        actual = simple_sort([1])
        expected = [1]
        self.assertEqual(actual, expected)

    def test_specified_list(self):
        actual = simple_sort([2,1,3,2,4,3,5,4,6,5,7,6,8,7,9,8])
        expected = [1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9]
        self.assertEqual(actual, expected)

    def test_compare_to_standard(self):
        rndn = [randint(0, 99) for _ in range(100)]
        actual = simple_sort(rndn)
        expected = sorted(rndn)
        self.assertEqual(actual, expected)

    def test_specified_list_reverse(self):
        actual = simple_sort([2,1,3,2,4,3,5,4,6,5,7,6,8,7,9,8], reverse=True)
        expected = [9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1]
        self.assertEqual(actual, expected)
    
    def test_compare_to_standard_reverse(self):
        rndn = [randint(0, 99) for _ in range(100)]
        actual = simple_sort(rndn, reverse=True)
        expected = sorted(rndn, reverse=True)
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main(verbosity=2)