from typing import List

from node import Node


class Queue:
    def __init__(self, queue: List[Node]=[]):
        self.queue = queue

    def enqueue(self, val):
        self.queue.append(val)
        return val

    def dequeue(self):
        if len(self.queue) == 0:
            raise ValueError('Can not dequeue empty queue')
        return self.queue.pop(0)

    def __contains__(self, node_id):
        return node_id in [n.id for n in self.queue]

    def __len__(self):
        return len(self.queue)

    def __repr__(self):
        return f'Queue({self.queue})'