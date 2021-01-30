import functools


def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.num_calls += 1
        return func(*args, **kwargs)

    wrapper.num_calls = 0
    return wrapper


@count_calls
def say_hi():
    print("Hi!")


say_hi()
say_hi()
print(say_hi.num_calls)
