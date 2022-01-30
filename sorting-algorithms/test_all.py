import unittest
from random import randint

from quick_sort import quick_sort
from merge_sort import merge_sort
from bubble_sort import bubble_sort
from simple_sort import simple_sort
from counting_sort import counting_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort

sort_algorithms = [bubble_sort, counting_sort, insertion_sort, quick_sort, selection_sort, simple_sort, merge_sort]


class TestAllSortingAlgorithms(unittest.TestCase):
    def test_empty_list(self):
        for alg in sort_algorithms:
            actual = alg([])
            expected = []
            self.assertEqual(actual, expected)

    def test_len_one_list(self):
        for alg in sort_algorithms:
            actual = alg([1])
            expected = [1]
            self.assertEqual(actual, expected)

    def test_specified_list(self):
        for alg in sort_algorithms:
            actual = alg([2,1,3,2,4,3,5,4,6,5,7,6,8,7,9,8])
            expected = [1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9]
            self.assertEqual(actual, expected)

    def test_compare_to_standard(self):
        for alg in sort_algorithms:
            rndn = [randint(0, 99) for _ in range(100)]
            actual = quick_sort(rndn)
            expected = sorted(rndn)
            self.assertEqual(actual, expected)

    def test_specified_list_reverse(self):
        for alg in sort_algorithms:
            actual = alg([2,1,3,2,4,3,5,4,6,5,7,6,8,7,9,8], reverse=True)
            expected = [9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1]
            self.assertEqual(actual, expected)
    
    def test_compare_to_standard_reverse(self):
        for alg in sort_algorithms:
            rndn = [randint(0, 99) for _ in range(100)]
            actual = quick_sort(rndn, reverse=True)
            expected = sorted(rndn, reverse=True)
            self.assertEqual(actual, expected)

    def test_compare_to_standard_n_lists(self):
        for alg in sort_algorithms:
            n = 100
            for i in range(n):
                rndn = [randint(0, 99) for _ in range(100)]
                actual = alg(rndn)
                expected = sorted(rndn)
                self.assertEqual(actual, expected)

    def test_compare_to_standard_n_lists_reverse(self):
        for alg in sort_algorithms:
            n = 100
            for i in range(n):
                rndn = [randint(0, 99) for _ in range(100)]
                actual = quick_sort(rndn, reverse=True)
                expected = sorted(rndn, reverse=True)
                self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)