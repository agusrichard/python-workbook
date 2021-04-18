import pytest
import numpy as np
from doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList:
    def test_iter(self):
        lst = list(range(10))
        linkedlist = DoublyLinkedList(lst)
        for index, value in enumerate(linkedlist):
            assert value == lst[index]

    def test_is_empty(self):
        linkedlist = DoublyLinkedList()
        assert linkedlist.is_empty()

    def test_len(self):
        lst = list(range(10))
        linkedlist = DoublyLinkedList(lst)
        assert len(linkedlist) == len(lst)

    def test_num_nodes(self):
        lst = list(range(10))
        linkedlist = DoublyLinkedList(lst)
        assert linkedlist.num_nodes == len(lst)

    def test_raise_error_when_assign_to_num_nodes(self):
        linkedlist = DoublyLinkedList()
        with pytest.raises(RuntimeError):
            linkedlist.num_nodes = 10

    def test_iter_random_numbers(self):
        random_numbers = np.random.randint(10, size=10)
        linkedlist = DoublyLinkedList()
        for index, value in enumerate(linkedlist):
            assert value == random_numbers[index]
