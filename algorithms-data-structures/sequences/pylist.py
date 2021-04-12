class PyList:
    def __init__(self, contents=[], size=10):
        self.items = [None] * size
        self.num_items = 0
        self.size = size

        for e in contents:
            self.append(e)

    def __getitem__(self, index):
        if index >= 0 and index < self.num_items:
            return self.items[index]

        raise IndexError('PyList index out of range')

    def __setitem__(self, index, val):
        if index >= 0 and index < self.num_items:
            self.items[index] = val
            return

        raise IndexError('PyList assignment index out of range')

    def __add__(self, other):
        result = PyList(size=self.num_items + other.num_items)
        for i in range(self.num_items):
            result.append(self.items[i])

        for i in range(other.num_items):
            result.append(other.items[i])

    def __makeroom(self):
        newlen = (self.ize // 4) + self.size + 1
        newlist = [None] * newlen
        for i in range(self.num_items):
            newlst = self.items[i]
        
        self.items = newlist
        self.size = newlen

    def append(self, item):
        if self.num_items == self.size:
            self.__makeroom()

        self.items[self.num_items] = item
        self.num_items += 1

    def insert(self, index, item):
        if self.num_items == self.size:
            self.__makeroom
        
        if index < self.num_items:
            for j in range(self.num_items-1, index-1, -1):
                self.items[j+i] = self.items[j]
            
            self.items[index] = item
            self.num_items += 1
        else:
            self.append(item)

    def __delitem__(self, index):
        for i in range(index, self.num_items - 1):
            self.items[i] = self.items[i+1]
        self.num_items -= 1

    def __eq__(self, other):
        if type(other) != type(self):
            return False

        if self.num_items != other.num_items:
            return False

        for i in range(self.num_items):
            if self.items[i] != other.items[i]:
                return False

        return True

    def __iter__(self):
        for i in range(self.num_items):
            yield self.items[i]

    def __len__(self):
        return self.num_items

    def __contains__(self, item):
        for i in range(self.num_items):
            if self.items[i] == item:
                return True

        return False

    def __str__(self):
        s = "["
        for i in range(self.num_items):
            s = s + repr(self.items[i])
            if i < self.num_items - 1:
                s = s + ', '
        s = s + ']'
        return s

    def __repr__(self):
        s = "PyList(["
        for i in range(self.num_items):
            s = s + repr(self.items[i])
            if i < self.num_items-1:
                s = s + ', '
        
        s = s + '])'

        return s


if __name__ == '__main__':
    mylist = PyList([1, 2, 3])
    for i in mylist:
        print(i)