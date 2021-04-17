import pytest
import numpy as np
from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList:
    def test_num_nodes_success(self):
        for i in range(10):
            lst = list(range(i))
            linkedlist = SinglyLinkedList(lst)

            assert linkedlist.num_nodes == i

    def test_indexing_success(self):
        linkedlist = SinglyLinkedList(list(range(10)))
        for i in range(10):
            assert linkedlist[i] == i

    def test_indexing_error(self):
        linkedlist = SinglyLinkedList([1, 2, 3])
        with pytest.raises(IndexError):
            linkedlist[5]
        with pytest.raises(IndexError):
            linkedlist[-1]

    def test_empty(self):
        linkedlist = SinglyLinkedList()
        assert linkedlist.num_nodes == 0
        assert list(linkedlist) == []
        assert str(linkedlist) == "SinglyLinkedList([])"
        assert linkedlist.is_empty()

    def test_random_nparray_to_SinglyLinkedList(self):
        lst = np.random.randint(10, size=10)
        linkedlist = SinglyLinkedList(list(lst))
        for i in range(len(lst)):
            assert linkedlist[i] == lst[i]

    def test_num_nodes_raised_error_when_do_assignment(self):
        with pytest.raises(RuntimeError):
            linkedlist = SinglyLinkedList([1, 2, 3])
            linkedlist.num_nodes = 0

    def test_str(self):
        for i in range(10):
            lst = list(range(i))
            linkedlist = SinglyLinkedList(lst)

            assert str(linkedlist) == "SinglyLinkedList({})".format(lst)

    def test_append_start_empty(self):
        linkedlist = SinglyLinkedList()
        linkedlist.append(1)
        assert linkedlist[0] == 1
        linkedlist.append(2)
        assert linkedlist[1] == 2
        linkedlist.append(10)
        assert linkedlist[2] == 10
        assert linkedlist.num_nodes == 3
        assert len(linkedlist) == 3

    def test_append_start_filled(self):
        linkedlist = SinglyLinkedList([1, 2, 3, 4, 5])
        linkedlist.append(6)
        assert linkedlist[5] == 6
        linkedlist.append("hello")
        assert linkedlist[6] == "hello"

    def test_concatenate(self):
        linkedlist1 = SinglyLinkedList([0, 1, 2, 3, 4])
        linkedlist2 = SinglyLinkedList([5, 6, 7])
        new_linkedlist = linkedlist1 + linkedlist2
        assert list(new_linkedlist) == list(range(8))

    def test_equality_same_SingleLinkedList(self):
        linkedlist1 = SinglyLinkedList([1, 2, 3])
        linkedlist2 = SinglyLinkedList([1, 2, 3])
        assert linkedlist1 == linkedlist2

    def test_inequality_type(self):
        lst = list(range(10))
        linkedlist = SinglyLinkedList(lst)
        assert linkedlist != lst

    def test_inequality_length(self):
        linkedlist1 = SinglyLinkedList([1, 2, 3, 4])
        linkedlist2 = SinglyLinkedList([1, 2, 3])
        assert linkedlist1 != linkedlist2

    def test_insert_from_empty(self):
        linkedlist = SinglyLinkedList()
        with pytest.raises(IndexError):
            linkedlist.insert(0, 0)

    def test_insert_filled_index_0(self):
        linkedlist = SinglyLinkedList([1, 2, 3, 4, 5])
        linkedlist.insert(0, 99)
        assert linkedlist[0] == 99
        assert len(linkedlist) == 6

    def test_insert_filled_index_last(self):
        linkedlist = SinglyLinkedList([1, 2, 3, 4, 5])
        linkedlist.insert(4, 99)
        assert linkedlist[4] == 99
        assert len(linkedlist) == 6

    def test_remove_from_empty(self):
        linkedlist = SinglyLinkedList()
        with pytest.raises(RuntimeError):
            linkedlist.remove(0)
