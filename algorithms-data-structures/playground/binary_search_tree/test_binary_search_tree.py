import pytest
from binary_search_tree import BinarySearchTree


class TestBinarySearchTree:
    def test_initialize_empty(self):
        bst = BinarySearchTree()

    def test_initialize_filled(self):
        bst = BinarySearchTree([1, 2, 3])