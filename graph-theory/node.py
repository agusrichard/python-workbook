from typing import Set


class Node:
    def __init__(self, id: int, value: int, neighbors: Set['Node']):
        self.id = id
        self.value = value
        self.neighbors = neighbors

    def __repr__(self):
        return f'Node({self.id}, {self.value})'

    def add_nodes(self, *nodes: 'Node'):
        for n in nodes:
            self.neighbors.add(n)