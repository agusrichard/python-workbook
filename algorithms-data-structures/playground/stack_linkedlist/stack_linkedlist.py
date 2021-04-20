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


class StackLinkedList:
    def __init__(self, contents: list = []):
        self.__head = DoublyNode()
        self.__tail = DoublyNode()
        self.__head.set_next(self.__tail)
        self.__tail.set_previous(self.__head)
        self.__num_nodes = 0

        if len(contents) != 0:
            for item in contents:
                self.push(item)

    def push(self, item: any) -> void:
        node = DoublyNode()
        tobe_changed_tail = self.__tail
        self.__tail.set_value(item)
        self.__tail.set_next(node)
        self.__tail = node
        self.__tail.set_previous(tobe_changed_tail)
        self.__num_nodes += 1

    def pop(self) -> any:
        if self.__num_nodes == 0:
            raise RuntimeError("Attempt to pop empty stack")
        last_node = self.__tail.get_previous()
        value = last_node.get_value()
        last_node.get_previous().set_next(self.__tail)

        del last_node
        self.__num_nodes -= 1
        return value

    def __iter__(self) -> Generator[any, None, None]:
        current_node = self.__head.get_next()
        while not current_node.is_empty():
            value = current_node.get_value()
            current_node = current_node.get_next()
            yield value

    def __str__(self) -> str:
        if self.__num_nodes == 0:
            return "StackLinkedList([])"

        result = "StackLinkedList(["
        for item in self:
            result += repr(item)
            result += ", "

        result = result[:-2]
        result = result + "])"

        return result

    def is_empty(self) -> bool:
        return self.__num_nodes == 0

    def __len__(self) -> int:
        return self.__num_nodes

    def __contains__(self, item: any) -> bool:
        for element in self:
            if element == item:
                return True

        return False

    def __eq__(self, other: QueueLinkedList) -> bool:
        if type(self) != type(other):
            return False

        if self.__num_nodes != other.__num_nodes:
            return False

        for i in range(self.__num_nodes):
            if (
                self.__find_node_by_index(i).get_value()
                != other.__find_node_by_index(i).get_value()
            ):
                return False

        return True

    def __find_node_by_index(self, index: int) -> DoublyNode:
        if index < 0 or index > self.__num_nodes - 1:
            raise IndexError("StackLinkedList index is out of scope")

        middle_point = self.__num_nodes // 2
        if index <= middle_point:
            current_node = self.__head.get_next()
            for i in range(index):
                current_node = current_node.get_next()
        else:
            current_node = self.__tail.get_previous()
            for i in range(self.__num_nodes - (index + 1)):
                current_node = current_node.get_previous()

        return current_node