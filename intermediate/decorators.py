import functools

def repeat(num_times=10):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(100)
def sayhi():
    print('Hi!')


sayhi()