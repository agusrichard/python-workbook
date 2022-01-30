import unittest
from time import time
from random import randint

from quick_sort import quick_sort
from merge_sort import merge_sort
from radix_sort import radix_sort
from bubble_sort import bubble_sort
from simple_sort import simple_sort
from counting_sort import counting_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from random_quick_sort import random_quick_sort


class TestAllSortingAlgorithms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sorting_algorithms = [
            merge_sort,
            quick_sort,
            radix_sort,
            bubble_sort,
            simple_sort,
            counting_sort,
            insertion_sort,
            selection_sort,
            random_quick_sort
        ]
        cls.durations = [[] for _ in range(len(cls.sorting_algorithms))]
        cls.list_max_value = 999999
        cls.reps = 100
        cls.list_length = 100

    def test_empty_list(self):
        for i, alg in enumerate(self.sorting_algorithms):
            start = time()
            actual = alg([])
            self.durations[i] = self.durations[i] + [(time()-start) * 1000]
            expected = []
            self.assertEqual(actual, expected)

    def test_len_one_list(self):
        for i, alg in enumerate(self.sorting_algorithms):
            start = time()
            actual = alg([1])
            self.durations[i] = self.durations[i] + [(time()-start) * 1000]
            expected = [1]
            self.assertEqual(actual, expected)

    def test_specified_list(self):
        for i, alg in enumerate(self.sorting_algorithms):
            start = time()
            actual = alg([2,1,3,2,4,3,5,4,6,5,7,6,8,7,9,8])
            self.durations[i] = self.durations[i] + [(time()-start) * 1000]
            expected = [1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9]
            self.assertEqual(actual, expected)

    def test_compare_to_standard(self):
        for i, alg in enumerate(self.sorting_algorithms):
            rndn = [randint(0, self.list_max_value) for _ in range(self.list_length)]
            start = time()
            actual = alg(rndn)
            self.durations[i] = self.durations[i] + [(time()-start) * 1000]
            expected = sorted(rndn)
            self.assertEqual(actual, expected)

    def test_specified_list_reverse(self):
        for i, alg in enumerate(self.sorting_algorithms):
            start = time()
            actual = alg([2,1,3,2,4,3,5,4,6,5,7,6,8,7,9,8], reverse=True)
            self.durations[i] = self.durations[i] + [(time()-start) * 1000]
            expected = [9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1]
            self.assertEqual(actual, expected)
    
    def test_compare_to_standard_reverse(self):
        for i, alg in enumerate(self.sorting_algorithms):
            rndn = [randint(0, self.list_max_value) for _ in range(self.list_length)]
            start = time()
            actual = alg(rndn, reverse=True)
            self.durations[i] = self.durations[i] + [(time()-start) * 1000]
            expected = sorted(rndn, reverse=True)
            self.assertEqual(actual, expected)

    def test_compare_to_standard_n_lists(self):
        for i, alg in enumerate(self.sorting_algorithms):
            for _ in range(self.reps):
                rndn = [randint(0, self.list_max_value) for _ in range(self.list_length)]
                start = time()
                actual = alg(rndn)
                self.durations[i] = self.durations[i] + [(time()-start) * 1000]
                expected = sorted(rndn)
                self.assertEqual(actual, expected)

    def test_compare_to_standard_n_lists_reverse(self):
        for i, alg in enumerate(self.sorting_algorithms):
            for _ in range(self.reps):
                rndn = [randint(0, self.list_max_value) for _ in range(self.list_length)]
                start = time()
                actual = alg(rndn, reverse=True)
                self.durations[i] = self.durations[i] + [(time()-start) * 1000]
                expected = sorted(rndn, reverse=True)
                self.assertEqual(actual, expected)

    @classmethod
    def tearDownClass(cls):
        print('\n\n\n================ RESULT ================\n')
        records = []
        for i, durs in enumerate(cls.durations):
             avg = sum(durs) / len(durs)
             records.append((cls.sorting_algorithms[i].__name__,  avg,))
        
        records = sorted(records, key=lambda xs: xs[-1])
        for rec in records:
            print('{:<20}: {:>15} ms'.format(rec[0], round(rec[1], 5)))

if __name__ == '__main__':
    unittest.main(verbosity=2)