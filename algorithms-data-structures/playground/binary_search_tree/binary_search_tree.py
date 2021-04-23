from __future__ import annotations


class Node:
    def __init__(self):
        self.__value: int = None
        self.__left: Node = None
        self.__right: Node = None

    def is_empty(self) -> bool:
        return self.__value == None

    def set_value(self, value: int) -> void:
        self.__value = value

    def set_left(self, node: Node) -> void:
        self.__left = node

    def set_right(self, node: Node) -> void:
        self.__right = node

    def get_value(self) -> int:
        return self.__value

    def get_left(self) -> Node:
        return self.__left

    def get_right(self) -> Node:
        return self.__right

    def __str__(self):
        return f"Node({self.__value})"


class BinarySearchTree:
    def __init__(self, contents: list = []):
        self.__root = None
        self.__num_nodes = 0

        if len(contents) != 0:
            for item in contents:
                self.insert(self.__root, item)

    def insert(self, node: Node, item: int) -> void:
        print(node)
        if node == None:
            node = Node()
            node.set_value(item)
            return node

        if item < node.get_value():
            node.set_left(self.insert(self, node.get_left(), item))
        else:
            node.set_right(self.insert(self, node.get_right(), item))

        return node


if __name__ == "__main__":
    bst = BinarySearchTree([1, 2, 3])
    print(bst)
