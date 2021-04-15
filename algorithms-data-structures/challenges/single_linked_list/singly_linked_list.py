from __future__ import annotations


class SinglyNode:
    def __init__(self):
        self.__item = None
        self.__next = None

    def get_item(self):
        return self.__item

    def set_item(self, item: any):
        self.__item = item

    def get_next(self):
        return self.__next

    def set_next(self, nxt: SinglyNode):
        self.__next = nxt

    def is_empty(self):
        return self.__item == None

    def __str__(self):
        return f"SinglyNode({self.get_item()})"


class SinglyLinkedList:
    def __init__(self, contents: list = []):
        self.head = SinglyNode()
        self.tail = SinglyNode()
        self.head.set_next(self.tail)
        self.num_items = 0

        if len(contents) != 0:
            for item in contents:
                self.append(item)

    def append(self, item: any):
        node = SinglyNode()
        self.tail.set_item(item)
        self.tail.set_next(node)
        self.tail = node
        self.num_items += 1

    def __iter__(self):
        current_node = self.head.get_next()
        while not current_node.is_empty():
            value = current_node.get_item()
            current_node = current_node.get_next()
            yield value

    def __getitem__(self, index: int):
        if index < 0 or index > self.num_items - 1:
            raise IndexError("SinglyLinkedList index is out of scope")
        current_node = self.head.get_next()
        for i in range(index):
            current_node = current_node.get_next()

        return current_node.get_item()

    def __setitem__(self, index: int, value: any):
        if index < 0 or index > self.num_items - 1:
            raise IndexError("SinglyLinkedList assignment index is out of scope")
        current_node = self.head.get_next()
        for i in range(index):
            current_node = current_node.get_next()

        current_node.set_item(value)


if __name__ == "__main__":
    linkedlist = SinglyLinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # print(linkedlist[9])
    linkedlist[0] = 99
    linkedlist[9] = 100
    for i in linkedlist:
        print(i)
