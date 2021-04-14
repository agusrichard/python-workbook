memo = dict()


def fibonacci(n):
    if n in memo:
        return memo[n]

    if n == 0:
        return 0

    if n == 1:
        return 1

    val = fibonacci(n - 1) + fibonacci(n - 2)
    memo[n] = val

    return val


if __name__ == "__main__":
    print(fibonacci(100))