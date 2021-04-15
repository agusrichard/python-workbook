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
        self.tail = self.head
        self.__num_items = 0

        if len(contents) != 0:
            for item in contents:
                self.append(item)

    def append(self, item: any):
        node = SinglyNode()
        if self.head.is_empty():
            self.tail = node
            self.head.set_item(item)
            self.head.set_next(self.tail)
        else:
            self.tail.set_next(node)
            self.tail.set_item(item)

        print("self.head.get_next() is self.tail", self.head.get_next() is self.tail)
        print("self.head", self.head)
        print("self.tail", self.tail)

    def __iter__(self):
        current_node = self.head
        while not current_node.is_empty():
            value = current_node.get_item()
            current_node = current_node.get_next()
            yield value


if __name__ == "__main__":
    linkedlist = SinglyLinkedList([1, 2, 3])
    for i in linkedlist:
        print(i)
    # print(linkedlist.head)
    # print(linkedlist.head.get_next())
    # print(linkedlist.head.get_next().get_item())
    # print(linkedlist.tail.get_item())