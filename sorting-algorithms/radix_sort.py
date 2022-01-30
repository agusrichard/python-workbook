import unittest
from typing import List
from random import randint


def radix_sort(lst: List, reverse=False) -> List:
    """Implement Radix Sort Algorithm"""
    converted = [str(i) for i in lst]
    temp = [[] for _ in range(10)]
    i = -1
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for item in converted:
            for index in range(10):
                try:
                    if int(item[i]) == index:
                        temp[index] = temp[index] + [item]
                        is_sorted = False
                        break
                except IndexError:
                    temp[0] = temp[0] + [item]
                    break

        converted = []
        for k, val in enumerate(temp):
            converted = converted + [*val]
            temp[k] = []
        i -= 1

    return [int(x) for x in converted]




class TestRadixSort(unittest.TestCase):
    def test_empty_list(self):
        actual = radix_sort([])
        expected = []
        self.assertEqual(actual, expected)

    def test_len_one_list(self):
        actual = radix_sort([1])
        expected = [1]
        self.assertEqual(actual, expected)

    def test_specified_list(self):
        actual = radix_sort([2,1,3,2,4,3,5,4,6,5,7,6,8,7,9,8])
        expected = [1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9]
        self.assertEqual(actual, expected)

    def test_compare_to_standard(self):
        rndn = [randint(0, 99) for _ in range(100)]
        actual = radix_sort(rndn)
        expected = sorted(rndn)
        self.assertEqual(actual, expected)

    # def test_specified_list_reverse(self):
    #     actual = radix_sort([2,1,3,2,4,3,5,4,6,5,7,6,8,7,9,8], reverse=True)
    #     expected = [9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1]
    #     self.assertEqual(actual, expected)
    
    # def test_compare_to_standard_reverse(self):
    #     rndn = [randint(0, 99) for _ in range(100)]
    #     actual = radix_sort(rndn, reverse=True)
    #     expected = sorted(rndn, reverse=True)
    #     self.assertEqual(actual, expected)

    def test_compare_to_standard_n_lists(self):
        n = 100
        for i in range(n):
            rndn = [randint(0, 99) for _ in range(100)]
            actual = radix_sort(rndn)
            expected = sorted(rndn)
            self.assertEqual(actual, expected)

    # def test_compare_to_standard_n_lists_reverse(self):
    #     n = 100
    #     for i in range(n):
    #         rndn = [randint(0, 99) for _ in range(100)]
    #         actual = radix_sort(rndn, reverse=True)
    #         expected = sorted(rndn, reverse=True)
    #         self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # print(radix_sort([951, 760, 631, 312, 241, 550, 292, 97, 185, 554]))