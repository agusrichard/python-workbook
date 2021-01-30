import functools


def repeats(num_reps=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_reps):
                value = func(*args, **kwargs)
            return value

        return wrapper

    return decorator


@repeats(num_reps=2)
def say_hi():
    print("Hi!")


say_hi()