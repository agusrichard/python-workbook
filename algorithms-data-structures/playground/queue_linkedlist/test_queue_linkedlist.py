import pytest
import numpy as np
from queue_linkedlist import QueueLinkedList


class TestQueue:
    def test_initialize_empty(self):
        q = QueueLinkedList()

    def test_initialize_filled(self):
        q = QueueLinkedList([1, 2, 3, 4])

    def test_enqueue_start_empty(self):
        q = QueueLinkedList()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

    def test_enqueue_start_filled(self):
        q = QueueLinkedList([1, 2, 3, 4])
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

    def test_dequeue_start_empty(self):
        q = QueueLinkedList()
        with pytest.raises(RuntimeError):
            q.dequeue()

    def test_dequeue_start_filled(self):
        q = QueueLinkedList([1, 2, 3])
        q.dequeue()
        q.dequeue()
        q.dequeue()

    def test_attempt_to_dequeue_more_than_num_nodes(self):
        q = QueueLinkedList([1, 2, 3])
        with pytest.raises(RuntimeError):
            q.dequeue()
            q.dequeue()
            q.dequeue()
            q.dequeue()

    def test_iter(self):
        lst = list(range(10))
        q = QueueLinkedList(lst)
        for index, value in enumerate(q):
            assert value == lst[index]

    def test_is_empty(self):
        q = QueueLinkedList()
        assert q.is_empty()

    def test_len(self):
        lst = list(range(10))
        q = QueueLinkedList(lst)
        assert len(q) == len(lst)

    def test_iter_random_numbers(self):
        random_numbers = np.random.randint(10, size=10)
        q = QueueLinkedList(random_numbers)
        for index, value in enumerate(q):
            assert value == random_numbers[index]

    def test_str(self):
        q = QueueLinkedList([1, 2, 3, 4, 5])
        assert str(q) == "QueueLinkedList([1, 2, 3, 4, 5])"

    def test_equality(self):
        q1 = QueueLinkedList([1, 2, 3, 4])
        q2 = QueueLinkedList([1, 2, 3, 4])
        assert q1 == q2

    def test_inequality_type(self):
        q = QueueLinkedList([1, 2, 3, 4])
        lst = [1, 2, 3, 4]
        assert q != lst

    def test_inequality_length(self):
        q1 = QueueLinkedList([1, 2, 3, 4])
        q2 = QueueLinkedList([1, 2, 3, 4, 5])
        assert q1 != q2

    def test_contains_success(self):
        lst = list(range(10))
        q = QueueLinkedList(lst)
        for i in lst:
            assert i in q

    def test_contains_negative(self):
        q = QueueLinkedList([1, 2, 3, 4])
        assert 99 not in q