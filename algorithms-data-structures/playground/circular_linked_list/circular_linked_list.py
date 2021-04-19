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


class CircularLinkedList:
    def __init__(self, contents: list = []):
        self.__head = DoublyNode()
        self.__tail = DoublyNode()
        self.__head.set_next(self.__tail)
        self.__head.set_previous(self.__tail)
        self.__tail.set_next(self.__head)
        self.__tail.set_previous(self.__head)
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
        self.__tail.set_next(self.__head)
        self.__num_nodes += 1

    def __iter__(self) -> Generator[any, None, None]:
        current_node = self.__head.get_next()
        while not current_node.is_empty():
            value = current_node.get_value()
            current_node = current_node.get_next()
            yield value

    def __str__(self) -> str:
        if self.__num_nodes == 0:
            return "CircularLinkedList([])"

        result = "CircularLinkedList(["
        for item in self:
            result += repr(item)
            result += ", "

        result = result[:-2]
        result = result + "])"

        return result

    def __getitem__(self, index: int) -> any:
        found_node = self.__find_node_by_index(index)
        return found_node.get_value()

    def __setitem__(self, index: int, value: any) -> void:
        found_node = self.__find_node_by_index(index)
        found_node.set_value(value)
        return

    def __find_node_by_index(self, index: int) -> DoublyNode:
        if index < 0 or index > self.__num_nodes - 1:
            raise IndexError("DoublyLinkedList index is out of scope")

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

    def is_empty(self):
        return self.__num_nodes == 0

    def __len__(self):
        return self.__num_nodes

    def __eq__(self, other: CircularLinkedList) -> bool:
        if type(self) != type(other):
            return False

        if self.__num_nodes != other.__num_nodes:
            return False

        for i in range(self.__num_nodes):
            if self[i] != other[i]:
                return False

        return True

    def __contains__(self, item: any) -> bool:
        for element in self:
            if element == item:
                return True

        return False

    def __add__(self, other: DoublyNode) -> DoublyNode:
        if type(self) != type(other):
            raise TypeError(f"Concatenate undefined for {type(self)} and {type(other)}")

        linkedlist = CircularLinkedList()
        for item in self:
            linkedlist.append(item)

        for item in other:
            linkedlist.append(item)

        return linkedlist

    def insert(self, index, value: any) -> void:
        node = DoublyNode()
        node.set_value(value)

        if index == 0:
            tobe_replaced_node = self.__find_node_by_index(index)
            self.__head.set_next(node)
            node.set_next(tobe_replaced_node)
            node.set_previous(self.__head)
        else:
            previous_tobe_replaced_node = self.__find_node_by_index(index - 1)
            tobe_replaced_node = previous_tobe_replaced_node.get_next()
            previous_tobe_replaced_node.set_next(node)
            tobe_replaced_node.set_previous(node)
            node.set_next(tobe_replaced_node)

        self.__num_nodes += 1
        return

    def remove(self, index) -> any:
        if self.__num_nodes == 0:
            raise RuntimeError(
                "Attempt to remove an item from empty CircularLinkedList"
            )

        if index == 0:
            tobe_deleted_node = self.__head.get_next()
            following_tobe_deleted_node = tobe_deleted_node.get_next()
            self.__head.set_next(following_tobe_deleted_node)
        else:
            previous_tobe_deleted_node = self.__find_node_by_index(index - 1)
            tobe_deleted_node = previous_tobe_deleted_node.get_next()
            following_tobe_deleted_node = tobe_deleted_node.get_next()
            previous_tobe_deleted_node.set_next(following_tobe_deleted_node)

        value = tobe_deleted_node.get_value()
        del tobe_deleted_node
        self.__num_nodes -= 1

        return value

    def pop(self) -> any:
        previous_last_node = self.__find_node_by_index(self.__num_nodes - 2)
        last_node = previous_last_node.get_next()
        value = last_node.get_value()
        previous_last_node.set_next(DoublyNode())

        del last_node
        self.__num_nodes -= 1
        return value

    @property
    def num_nodes(self):
        return self.__num_nodes

    @num_nodes.setter
    def num_nodes(self, value: any):
        raise RuntimeError("Can not assign to num_nodes property")


if __name__ == "__main__":
    pass