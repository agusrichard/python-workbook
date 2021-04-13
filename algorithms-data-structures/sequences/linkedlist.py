class LinkedList:
    class __Node:
        def __init__(self, item, nxt=None):
            self.item = item
            self.next = nxt

        def get_item(self):
            return self.item

        def get_next(self):
            return self.next

        def set_item(self, item):
            self.item = item

        def set_next(self, nxt):
            self.next = nxt

    def __init__(self, contents=[]):
        self.first = LinkedList.__Node(None, None)
        self.last = self.first
        self.num_items = 0

        for e in contents:
            self.append(e)

    def __getitem__(self, index):
        if index >= 0 and index < self.num_items:
            cursor = self.first.get_next()
            for i in range(index):
                cursor = cursor.get_next()

            return cursor.get_item()

        raise IndexError("LinkedList index out of scope")

    def __setitem__(self, index, value):
        if index >= 0 and index < self.num_items:
            cursor = self.first.get_next()
            for i in range(index):
                cursor.get_next()

            cursor.set_item(value)
            return

        raise IndexError("LinkedList assignment index out of range")

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError(
                "Concatenate undefined for "
                + str(type(self))
                + " + "
                + str(type(other))
            )

        result = LinkedList()
        cursor = result.first.get_next()

        while cursor != None:
            result.append(cursor.get_item())
            cursor = cursor.get_next()

        cursor = other.first.get_next()

        while cursor != None:
            result.append(cursor.get_item())
            cursor = cursor.get_next()

        return result

    def append(self, item):
        node = LinkedList.__Node(item)
        self.last.set_next(node)
        self.last = node
        self.num_items += 1

    def insert(self, index, item):
        cursor = self.first

        if index < self.num_items:
            for i in range(index):
                cursor = cursor.get_next()

            node = LinkedList.__Node(item, cursor.get_next())
            cursor.set_next(node)
            self.num_items += 1
        else:
            self.append(item)
