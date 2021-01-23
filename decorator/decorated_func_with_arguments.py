import functools


def do_ten_times(func):
    """Repeats func ten times"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(10):
            func(*args, **kwargs)

    return wrapper


@do_ten_times
def introduce_myself(name):
    print(f"Hi, my name is {name}")


introduce_myself("John")