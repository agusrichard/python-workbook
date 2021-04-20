import pytest
import numpy as np
from stack_linkedlist import StackLinkedList


class TestStackLinkedList:
    def test_initialize_start_empty(self):
        stack = StackLinkedList()

    def test_initialize_start_filled(self):
        stack = StackLinkedList([1, 2, 3])

    def test_push_start_empty(self):
        stack = StackLinkedList()
        stack.push(1)
        stack.push(2)
        stack.push(3)

    def test_push_start_filled(self):
        stack = StackLinkedList([1, 2, 3])
        stack.push(1)
        stack.push(2)
        stack.push(3)

    def test_pop_start_empty(self):
        q = StackLinkedList()
        with pytest.raises(RuntimeError):
            q.pop()

    def test_pop_start_filled(self):
        q = StackLinkedList([1, 2, 3])
        q.pop()
        q.pop()
        q.pop()

    def test_attempt_to_pop_more_than_num_nodes(self):
        q = StackLinkedList([1, 2, 3])
        with pytest.raises(RuntimeError):
            q.pop()
            q.pop()
            q.pop()
            q.pop()

    def test_iter(self):
        lst = list(range(10))
        q = StackLinkedList(lst)
        for index, value in enumerate(q):
            assert value == lst[index]

    def test_iter_random_numbers(self):
        random_numbers = np.random.randint(10, size=10)
        q = StackLinkedList(random_numbers)
        for index, value in enumerate(q):
            assert value == random_numbers[index]

    def test_is_empty(self):
        q = StackLinkedList()
        assert q.is_empty()

    def test_len(self):
        lst = list(range(10))
        q = StackLinkedList(lst)
        assert len(q) == len(lst)

    def test_str(self):
        q = StackLinkedList([1, 2, 3, 4, 5])
        assert str(q) == "StackLinkedList([1, 2, 3, 4, 5])"

    def test_equality(self):
        q1 = StackLinkedList([1, 2, 3, 4])
        q2 = StackLinkedList([1, 2, 3, 4])
        assert q1 == q2

    def test_inequality_type(self):
        q = StackLinkedList([1, 2, 3, 4])
        lst = [1, 2, 3, 4]
        assert q != lst

    def test_inequality_length(self):
        q1 = StackLinkedList([1, 2, 3, 4])
        q2 = StackLinkedList([1, 2, 3, 4, 5])
        assert q1 != q2

    def test_contains_success(self):
        lst = list(range(10))
        q = StackLinkedList(lst)
        for i in lst:
            assert i in q

    def test_contains_negative(self):
        q = StackLinkedList([1, 2, 3, 4])
        assert 99 not in q