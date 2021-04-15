import pytest
from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList:
    def test_num_items_success(self):
        for i in range(10):
            lst = list(range(i))
            linkedlist = SinglyLinkedList(lst)

            assert linkedlist.num_items == i

    def test_num_items_raised_error_when_do_assignment(self):
        with pytest.raises(RuntimeError):
            linkedlist = SinglyLinkedList([1, 2, 3])
            linkedlist.num_items = 0

    def test_SinglyLinkedList_str(self):
        for i in range(10):
            lst = list(range(i))
            linkedlist = SinglyLinkedList(lst)

            assert str(linkedlist) == "SinglyLinkedList({})".format(lst)
