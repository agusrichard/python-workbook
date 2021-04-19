import pytest
import numpy as np
from circular_linked_list import CircularLinkedList


class TestCircularLinkedList:
    def test_initialize_empty_linkedlist(self):
        linkedlist = CircularLinkedList()

    def test_iter(self):
        lst = list(range(10))
        linkedlist = CircularLinkedList(lst)
        for index, value in enumerate(linkedlist):
            assert value == lst[index]

    def test_is_empty(self):
        linkedlist = CircularLinkedList()
        assert linkedlist.is_empty()

    def test_len(self):
        lst = list(range(10))
        linkedlist = CircularLinkedList(lst)
        assert len(linkedlist) == len(lst)

    def test_num_nodes(self):
        lst = list(range(10))
        linkedlist = CircularLinkedList(lst)
        assert linkedlist.num_nodes == len(lst)

    def test_raise_error_when_assign_to_num_nodes(self):
        linkedlist = CircularLinkedList()
        with pytest.raises(RuntimeError):
            linkedlist.num_nodes = 10

    def test_str(self):
        linkedlist = CircularLinkedList([1, 2, 3, 4, 5])
        assert str(linkedlist) == "CircularLinkedList([1, 2, 3, 4, 5])"

    def test_indexing_consecutive_sequence_success(self):
        linkedlist = CircularLinkedList(list(range(10)))
        for i in range(10):
            assert linkedlist[i] == i

    def test_indexing_random_numbers_success(self):
        random_numbers = np.random.randint(10, size=10)
        linkedlist = CircularLinkedList(random_numbers)
        for index, value in enumerate(random_numbers):
            assert linkedlist[index] == value

    def test_indexing_out_of_scope(self):
        linkedlist = CircularLinkedList(list(range(10)))
        with pytest.raises(IndexError):
            linkedlist[-10]
        with pytest.raises(IndexError):
            linkedlist[20]

    def test_index_assignment_success(self):
        lst1 = list(range(10))
        lst2 = sorted(lst1)
        linkedlist = CircularLinkedList(lst1)
        for i in range(len(lst1)):
            linkedlist[i] = lst2[i]
            assert linkedlist[i] == lst2[i]

        assert list(linkedlist) == lst2

    def test_index_assignment_out_of_index(self):
        lst = list(range(5))
        linkedlist = CircularLinkedList(lst)
        with pytest.raises(IndexError):
            linkedlist[99] = 0

    def test_equality(self):
        linkedlist1 = CircularLinkedList([1, 2, 3, 4])
        linkedlist2 = CircularLinkedList([1, 2, 3, 4])
        assert linkedlist1 == linkedlist2

    def test_inequality_type(self):
        linkedlist = CircularLinkedList([1, 2, 3, 4])
        lst = [1, 2, 3, 4]
        assert linkedlist != lst

    def test_inequality_length(self):
        linkedlist1 = CircularLinkedList([1, 2, 3, 4])
        linkedlist2 = CircularLinkedList([1, 2, 3, 4, 5])
        assert linkedlist1 != linkedlist2

    def test_contains_success(self):
        lst = list(range(10))
        linkedlist = CircularLinkedList(lst)
        for i in lst:
            assert i in linkedlist

    def test_contains_negative(self):
        linkedlist = CircularLinkedList([1, 2, 3, 4])
        assert 99 not in linkedlist

    def test_append_start_empty(self):
        linkedlist = CircularLinkedList()
        for i in range(10):
            linkedlist.append(i)

    def test_append_start_filled(self):
        linkedlist = CircularLinkedList([1, 2, 3])
        for i in range(10):
            linkedlist.append(i)

    def test_concatenate_success(self):
        linkedlist1 = CircularLinkedList([0, 1, 2])
        linkedlist2 = CircularLinkedList([3, 4, 5])
        new_linkedlist = linkedlist1 + linkedlist2
        assert list(new_linkedlist) == [0, 1, 2, 3, 4, 5]

    def test_concatenate_empty_and_filled(self):
        linkedlist1 = CircularLinkedList()
        linkedlist2 = CircularLinkedList([1, 2, 3])
        new_linkedlist = linkedlist1 + linkedlist2
        assert list(new_linkedlist) == [1, 2, 3]

    def test_concatenate_empty_and_filled(self):
        linkedlist1 = CircularLinkedList()
        linkedlist2 = CircularLinkedList()
        new_linkedlist = linkedlist1 + linkedlist2
        assert list(new_linkedlist) == []

    def test_insert_from_empty(self):
        linkedlist = CircularLinkedList()
        with pytest.raises(IndexError):
            linkedlist.insert(0, 0)

    def test_insert_filled_index_0(self):
        linkedlist = CircularLinkedList([1, 2, 3, 4, 5])
        linkedlist.insert(0, 99)
        assert linkedlist[0] == 99
        assert len(linkedlist) == 6

    def test_insert_filled_index_last(self):
        linkedlist = CircularLinkedList([1, 2, 3, 4, 5])
        linkedlist.insert(4, 99)
        assert linkedlist[4] == 99
        assert len(linkedlist) == 6

    def test_remove_from_empty(self):
        linkedlist = CircularLinkedList()
        with pytest.raises(RuntimeError):
            linkedlist.remove(0)

    def test_pop(self):
        linkedlist = CircularLinkedList([1, 2, 3, 4, 5])
        popped = linkedlist.pop()
        assert popped == 5
        assert len(linkedlist) == 4
        assert list(linkedlist) == [1, 2, 3, 4]