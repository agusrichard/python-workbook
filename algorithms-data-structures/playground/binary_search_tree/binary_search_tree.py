from __future__ import annotations


class Node:
    def __init__(self):
        self.__value: any = None
        self.__left: Node = None
        self.__right: Node = None

    def is_empty(self) -> bool:
        return self.__value == None

    def set_value(self, value: any) -> void:
        self.__value = value

    def set_left(self, node: Node) -> void:
        self.__left = node

    def set_right(self, node: Node) -> void:
        self.__right = node

    def get_value(self) -> any:
        return self.__value

    def get_left(self) -> Node:
        return self.__left

    def get_right(self) -> Node:
        return self.__right


class BinarySearchTree:
    def __init__(self, contents: list = []):
        self.__root = None
        self.__num_nodes = 0

        if len(contents) != 0:
            for item in contents:
                self.insert(item)

    def insert(self, item: any) -> void:
        node = self.__root
        self.__insert(node, item)

    def __insert(self, node: Node, value: any) -> void:
        if node == None:
            self.__create_node(value)

    def __create_node(self, parent_node: Node, item: any) -> Node:
        node = Node()
        node.set_left(None)
        node.set_right(None)
        node.set_value(item)
        return node


if __name__ == "__main__":
    print("Sekardayu Hana Pradiani")
