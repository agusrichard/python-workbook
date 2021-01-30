import functools
import time
import random


def do_ten_times(func):
    """Repeats func ten times"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(10):
            func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


def timer(func):
    """Returns the time it takes for some function to execute"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        interval = end - start
        print(
            f"The time function {func.__name__} took to be executed is {interval} secs"
        )
        return value

    return wrapper


@timer
@do_ten_times
def wasting_operations(reps=1000000):
    total = 0
    for i in range(reps):
        summation = sum([random.randint(0, 10) for j in range(10)])
        total += summation
    return total


print(wasting_operations(reps=1000))
