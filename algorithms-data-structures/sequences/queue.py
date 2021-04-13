class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0

    def __compress(self):
        newlst = []
        for i in range(self.front_index, len(self.items)):
            newlst.append(self.items[i])

        self.items = newlst
        self.front_index = 0

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Atempt to dequeue an empty queue")

        if self.front_index * 2 > len(self.items):
            self.__compress()

        item = self.items[self.front_index]
        self.front_index += 1
        return item

    def enqueue(self, item):
        self.items.append(item)

    def front(self):
        if self.is_empty():
            raise RuntimeError("Attempt to access front of empty queue")

        return self.items[self.front_index]

    def is_empty(self):
        return self.front_index == len(self.items)