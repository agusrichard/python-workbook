class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Attempt to pop an empty list")

        top_index = len(self.items) - 1
        item = self.items[top_index]
        del self.items[top_index]
        return item

    def push(self, item):
        self.items.append(item)

    def top(self):
        if self.is_empty():
            raise RuntimeError("Attempt to get top of empty stack")

        top_index = len(self.items) - 1
        return self.items[top_index]

    def is_empty(self):
        return len(self.items) == 0