from __future__ import annotations
from typing import Generator


class SinglyNode:
    def __init__(self):
        self.__item = None
        self.__next = None

    def get_item(self) -> any:
        return self.__item

    def set_item(self, item: any) -> void:
        self.__item = item

    def get_next(self) -> SinglyNode:
        return self.__next

    def set_next(self, nxt: SinglyNode) -> void:
        self.__next = nxt

    def is_empty(self) -> bool:
        return self.__item == None

    def __str__(self) -> str:
        return f"SinglyNode({self.get_item()})"


class SinglyLinkedList:
    def __init__(self, contents: list = []):
        self.__head = SinglyNode()
        self.__tail = SinglyNode()
        self.__head.set_next(self.__tail)
        self.__num_items = 0

        if len(contents) != 0:
            for item in contents:
                self.append(item)

    def append(self, item: any) -> void:
        node = SinglyNode()
        self.__tail.set_item(item)
        self.__tail.set_next(node)
        self.__tail = node
        self.__num_items += 1

    def __iter__(self) -> Generator[any, None, None]:
        current_node = self.__head.get_next()
        while not current_node.is_empty():
            value = current_node.get_item()
            current_node = current_node.get_next()
            yield value

    def __getitem__(self, index: int) -> any:
        found_node = self.__find_node_by_index(index)
        return found_node.get_item()

    def __setitem__(self, index: int, value: any) -> void:
        found_node = self.__find_node_by_index(index)
        found_node.set_item(value)
        return

    def __find_node_by_index(self, index) -> SinglyNode:
        if index < 0 or index > self.__num_items - 1:
            raise IndexError("SinglyLinkedList index is out of scope")
        current_node = self.__head.get_next()
        for i in range(index):
            current_node = current_node.get_next()

        return current_node

    def __add__(self, other: SinglyLinkedList) -> SinglyLinkedList:
        if type(self) != type(other):
            raise TypeError(f"Concatenate undefined for {type(self)} and {type(other)}")

        linkedlist = SinglyLinkedList()
        for item in self:
            linkedlist.append(item)

        for item in other:
            linkedlist.append(item)

        return linkedlist

    def __str__(self) -> str:
        if self.__num_items == 0:
            return "SinglyLinkedList([])"

        result = "SinglyLinkedList(["
        for item in self:
            result += repr(item)
            result += ", "

        result = result[:-2]
        result = result + "])"

        return result

    def __eq__(self, other: SinglyLinkedList) -> bool:
        if type(self) != type(other):
            return False

        if self.__num_items != other.__num_items:
            return False

        for i in range(self.__num_items):
            if self[i] != other[i]:
                return False

        return True

    def __len__(self):
        return self.__num_items

    def is_empty(self) -> bool:
        return self.__num_items == 0

    def insert(self, index, value: any) -> void:
        node = SinglyNode()
        node.set_item(value)

        if index == 0:
            tobe_replaced_node = self.__find_node_by_index(index)
            self.__head.set_next(node)
            node.set_next(tobe_replaced_node)
        else:
            previous_tobe_replaced_node = self.__find_node_by_index(index - 1)
            tobe_replaced_node = previous_tobe_replaced_node.get_next()
            previous_tobe_replaced_node.set_next(node)
            node.set_next(tobe_replaced_node)

        self.__num_items += 1
        return

    def remove(self, index) -> any:
        if self.__num_items == 0:
            raise RuntimeError("Attempt to remove an item from empty SinglyLinkedList")

        if index == 0:
            tobe_deleted_node = self.__head.get_next()
            following_tobe_deleted_node = tobe_deleted_node.get_next()
            self.__head.set_next(following_tobe_deleted_node)
        else:
            previous_tobe_deleted_node = self.__find_node_by_index(index - 1)
            tobe_deleted_node = previous_tobe_deleted_node.get_next()
            following_tobe_deleted_node = tobe_deleted_node.get_next()
            previous_tobe_deleted_node.set_next(following_tobe_deleted_node)

        value = tobe_deleted_node.get_item()
        del tobe_deleted_node
        self.__num_items -= 1

        return value

    def pop(self) -> any:
        previous_last_node = self.__find_node_by_index(self.__num_items - 2)
        last_node = previous_last_node.get_next()
        value = last_node.get_item()
        previous_last_node.set_next(SinglyNode())
        del last_node

        return value

    @property
    def num_items(self) -> int:
        return self.__num_items

    @num_items.setter
    def num_items(self, value: any):
        raise RuntimeError("Can not assign to num_items property")


if __name__ == "__main__":
    linkedlist = SinglyLinkedList()
    linkedlist.remove(0)
    # print(linkedlist)