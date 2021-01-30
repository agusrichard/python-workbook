import functools


def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.num_calls += 1
        return func(*args, **kwargs)

    wrapper.num_calls = 0
    return wrapper


@count_calls
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(20):
    print("i        :", i)
    print("Value    :", fibonacci(i))
    print("Num calls:", fibonacci.num_calls)
    fibonacci.num_calls = 0