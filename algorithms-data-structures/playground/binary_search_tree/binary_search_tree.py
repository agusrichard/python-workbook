from __future__ import annotations


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_empty(self) -> bool:
        return self.value == None

    def __str__(self):
        return f"Node({self.value})"


class BinarySearchTree:
    def __init__(self, contents: list = []):
        self.__root = None

        if len(contents) != 0:
            for item in contents:
                self.insert(item)

    def insert(self, value: int) -> void:
        self.__root = self.__insert(self.__root, value)

    @staticmethod
    def __insert(node: None, value: int) -> Node:
        if node == None:
            return Node(value)
        if value < node.value:
            node.left = BinarySearchTree.__insert(node.left, value)
        else:
            node.right = BinarySearchTree.__insert(node.right, value)

        return node

    def inorder_traversal(self):
        return self.__inorder_traversal(self.__root)

    @staticmethod
    def __inorder_traversal(root):
        if root is not None:
            yield from BinarySearchTree.__inorder_traversal(root.left)

            yield root.value

            yield from BinarySearchTree.__inorder_traversal(root.right)

    def __iter__(self):
        return self.__inorder_traversal(self.__root)

    # This contains method is not optimized. since we have to generate
    # the whole generator then check it one by one
    # it's better to use inorder traversal method to do the search
    def __contains__(self, value: int):
        for item in self:
            if item == value:
                return True


if __name__ == "__main__":
    bst = BinarySearchTree([1, 2, 3])
    print(bst.inorder_traversal())
    for i in bst.inorder_traversal():
        print(i)
