class TimesNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()


class PlusNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()


class NumNode:
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num


if __name__ == "__main__":
    x = NumNode(5)
    y = NumNode(6)
    p = PlusNode(x, y)
    t = TimesNode(p, NumNode(6))
    root = PlusNode(t, NumNode(3))

    print(root.eval())