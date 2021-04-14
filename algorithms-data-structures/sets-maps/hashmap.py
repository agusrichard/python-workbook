class HashMap:
    class __Placeholder:
        def __init__(self):
            pass

        def __eq__(self, other):
            return False

    def __init__(self, contents=[]):
        self.items = [None] * 10
        self.num_items = 0

        for item in contents:
            self.add(item)

    @staticmethod
    def __add(item, items):
        idx = hash(item) % len(items)
        loc = -1

        while items[idx] != None:
            if items[idx] == item:
                return False

            if loc < 0 and type(items[idx]) == HashMap.__Placeholder:
                loc = idx

            idx = (idx + 1) % len(items)

        if loc < 0:
            loc = idx

        items[loc] = item

        return True

    @staticmethod
    def __rehash(old_list, new_list):
        for x in old_list:
            if x != None and type(x) != HashMap.__Placeholder:
                HashMap.__add(x, new_list)

        return new_list

    def add(self, item):
        if HashMap.__add(item, self.items):
            self.num_items += 1
            load = self.num_items / len(self.items)
            if load >= 0.75:
                self.items = HashMap.__rehash(self.items, [None] * 2 * len(self.items))

    @staticmethod
    def __remove(item, items):
        idx = hash(item) % len(items)

        while items[idx] != None:
            if items[idx] == item:
                next_idx = (idx + 1) % len(items)
                if items[next_idx] == None:
                    items[idx] = None
                else:
                    items[idx] = HashMap.__Placeholder()
                return True

        return False

    def remove(self, item):
        if HashMap.__remove(item, self.items):
            self.num_items -= 1
            load = max(self.num_items, 10) / len(self.items)
            if load <= 0.25:
                self.items = HashMap.__rehash(
                    self.items, [None] * int(len(self.items) / 2)
                )
        else:
            raise KeyError("Item not in HashMap")

    def __contains__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx] != None:
            if self.items[idx] == item:
                return True

            idx = (idx + 1) % len(self.items)

        return False

    def __iter__(self):
        for i in range(len(self.items)):
            if self.items[i] != None and type(self.items[i]) != HashMap.__Placeholder:
                yield self.items[i]

    def __getitem__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx] != None:
            if self.items[idx] == item:
                return self.items[idx]

            idx = (idx + 1) % len(self.items)

        return None
