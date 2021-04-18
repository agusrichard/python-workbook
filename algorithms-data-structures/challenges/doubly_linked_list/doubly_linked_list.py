from __future__ import annotations
from typing import Generator


class DoublyNode:
    def __init__(self):
        self.__value = None
        self.__next = None
        self.__previous = None

    def get_value(self) -> any:
        return self.__value

    def set_value(self, value) -> void:
        self.__value = value

    def get_next(self) -> DoublyNode:
        return self.__next

    def set_next(self, nxt: DoublyNode) -> void:
        self.__next = nxt

    def get_previous(self) -> DoublyNode:
        return self.__previous

    def set_previous(self, previous: DoublyNode) -> void:
        self.__previous = previous

    def is_empty(self) -> bool:
        return self.__value == None

    def __str__(self) -> str:
        return f"DoublyNode({self.__value})"


class DoublyLinkedList:
    def __init__(self, contents: list = []):
        self.__head = DoublyNode()
        self.__tail = DoublyNode()
        self.__head.set_next(self.__tail)
        self.__num_nodes = 0

        if len(contents) != 0:
            for item in contents:
                self.append(item)

    def append(self, item: any) -> void:
        node = DoublyNode()
        tobe_changed_tail = self.__tail
        self.__tail.set_value(item)
        self.__tail.set_next(node)
        self.__tail = node
        self.__tail.set_previous(tobe_changed_tail)
        self.__num_nodes += 1

    def __iter__(self) -> Generator[any, None, None]:
        current_node = self.__head.get_next()
        while not current_node.is_empty():
            value = current_node.get_value()
            current_node = current_node.get_next()
            yield value

    def __find_node_by_index(self, index) -> SinglyNode:
        if index < 0 or index > self.__num_nodes - 1:
            raise IndexError("SinglyLinkedList index is out of scope")
        current_node = self.__head.get_next()
        for i in range(index):
            current_node = current_node.get_next()

    def is_empty(self):
        return self.__num_nodes == 0

    def __len__(self):
        return self.__num_nodes

    @property
    def num_nodes(self):
        return self.__num_nodes

    @num_nodes.setter
    def num_nodes(self, value: any):
        raise RuntimeError("Can not assign to num_nodes property")


if __name__ == "__main__":
    linkedlist = DoublyLinkedList(list(range(10)))
    for item in linkedlist:
        print(item)
