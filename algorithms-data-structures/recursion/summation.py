def normalSum(n):
    return n*(n + 1) / 2

def recSum(n):
    if n == 0:
        return 0
    return n + recSum(n - 1)


if __name__ == '__main__':
    print(normalSum(10))
    print(recSum(10))