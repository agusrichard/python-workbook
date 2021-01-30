import functools


def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.num_calls += 1
        return func(*args, **kwargs)

    wrapper.num_calls = 0
    return wrapper


def cache(func):
    """Keep a cache of previous function calls"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args, **kwargs)
        return wrapper.cache[cache_key]

    wrapper.cache = dict()
    return wrapper


@count_calls
@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(19))
print(fibonacci.num_calls)
