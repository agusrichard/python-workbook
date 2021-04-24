import pytest
import numpy as np
from binary_search_tree import BinarySearchTree


class TestBinarySearchTree:
    def test_initialize_empty(self):
        bst = BinarySearchTree()

    def test_initialize_filled(self):
        bst = BinarySearchTree([1, 2, 3])

    def test_insert_start_emtpy(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)

    def test_insert_start_filled(self):
        bst = BinarySearchTree([1, 2, 3])
        bst.insert(4)
        bst.insert(5)
        bst.insert(6)

    def test_iter_empty(self):
        bst = BinarySearchTree()
        for item in bst:
            assert item

    def test_iter_filled(self):
        lst = sorted([1, 2, 3, 4, 5])
        bst = BinarySearchTree(lst)
        for index, value in enumerate(bst):
            assert value == lst[index]

    def test_iter_filled_random_number(self):
        random_numbers = np.random.randint(100, size=10)
        random_numbers.sort()
        bst = BinarySearchTree(random_numbers)
        for index, value in enumerate(bst):
            assert value == random_numbers[index]

    def test_contains(self):
        lst = [1, 2, 3, 4, 5]
        bst = BinarySearchTree(lst)
        for item in lst:
            assert item in bst

    def test_contains_random(self):
        random_numbers = np.random.randint(100, size=10)
        bst = BinarySearchTree(random_numbers)
        for item in random_numbers:
            assert item in bst