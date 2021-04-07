class MyList:
    def __init__(self):
        self.items = []

    # def append(self, item):
    #     """
    #         time complexity for this method is O(n^2)
    #     """
    #     self.items = self.items + [item]

    def append(self, item):
        """A better way to append item to a list"""
        self.items.append(item)

if __name__ == '__main__':
    lst = MyList()
    lst.append(0)
    lst.append(1)
    lst.append(2)

    print(lst.items)