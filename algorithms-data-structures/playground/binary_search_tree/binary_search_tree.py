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
        self.root = None

        if len(contents) != 0:
            for item in contents:
                self.insert(item)

    def insert(self, item: int) -> void:
        self.root = self.__insert(self.root, item)

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
        return self.__inorder(self.root)

    @staticmethod
    def __inorder(root):
        if root is not None:
            # Traverse left
            yield from BinarySearchTree.__inorder(root.left)

            yield root.value

            # Traverse right
            yield from BinarySearchTree.__inorder(root.right)


if __name__ == "__main__":
    bst = BinarySearchTree([1, 2, 3])
    print(bst.root)
    print(bst.inorder_traversal())
    for i in bst.inorder_traversal():
        print(i)
