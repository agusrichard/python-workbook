class PyList:
    def __init__(self, size=1):
        self.items = [None] * size
        self.num_items = 0

    def append(self, item):
        if self.num_items == len(self.items):
            newlist = [None] * self.num_items * 2
            for i in range(len(self.items)):
                newlist[i] = self.items[i]
            
            self.items = newlist
        
        self.items[self.num_items] = item
        self.num_items += 1


if __name__ == '__main__':
    mylist = PyList()

    for i in range(100):
        mylist.append(i)
    print(mylist.items)
    print(mylist.num_items)
    print(len(mylist.items))