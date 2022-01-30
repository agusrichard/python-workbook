import unittest
from typing import List
from random import randint

def counting_sort(lst: List, reverse=False) -> List:
    """Implement Counting Sort Algorithm"""
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return lst

    max_value = max(lst)
    min_value = min(lst)
    length = max_value - min_value

    counter = [0 for _ in range(length+1)]
    result = [0 for _ in range(len(lst))]
    
    # Make sure that lst always start 
    updated_lst = [i-min_value for i in lst]

    # Fill up the counter list
    for i in updated_lst:
        counter[i] += 1

    if not reverse:
        for i in range(len(counter)-1):
            counter[i+1] = counter[i+1] + counter[i]

        for i in range(1, len(counter)):
            counter[-i] = counter[-(i+1)]
        counter[0] = 0
    else:
        for i in range(1, len(counter)):
            counter[-(i+1)] = counter[-i] + counter[-(i+1)]

        for i in range(len(counter)-1):
            counter[i] = counter[i+1]
        counter[-1] = 0

    for i, j in zip(updated_lst, lst):
        position = counter[i]
        result[position] = j
        counter[i] += 1

    return result



class CountingSortTest(unittest.TestCase):
    def test_empty_list(self):
        actual = counting_sort([])
        expected = []
        self.assertEqual(actual, expected)

    def test_len_one_list(self):
        actual = counting_sort([1])
        expected = [1]
        self.assertEqual(actual, expected)

    def test_specified_list(self):
        actual = counting_sort([2,1,0,3,2,4,3,5,4,6,5,7,6,8,7,9,8])
        expected = [0,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9]
        self.assertEqual(actual, expected)

    def test_compare_to_standard(self):
        rndn = [randint(0, 99) for _ in range(100)]
        actual = counting_sort(rndn)
        expected = sorted(rndn)
        self.assertEqual(actual, expected)

    def test_specified_list_reverse(self):
        actual = counting_sort([2,1,3,2,4,3,5,4,6,5,7,6,8,7,9,8], reverse=True)
        expected = [9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1]
        self.assertEqual(actual, expected)
    
    def test_compare_to_standard_reverse(self):
        rndn = [randint(0, 99) for _ in range(100)]
        actual = counting_sort(rndn, reverse=True)
        expected = sorted(rndn, reverse=True)
        self.assertEqual(actual, expected)

    def test_compare_to_standard_n_lists(self):
        n = 100
        for i in range(n):
            rndn = [randint(0, 99) for _ in range(100)]
            actual = counting_sort(rndn)
            expected = sorted(rndn)
            self.assertEqual(actual, expected)

    def test_compare_to_standard_n_lists_reverse(self):
        n = 100
        for i in range(n):
            rndn = [randint(0, 99) for _ in range(100)]
            actual = counting_sort(rndn, reverse=True)
            expected = sorted(rndn, reverse=True)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)