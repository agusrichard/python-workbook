def simple_decorator(func):
    def wrapper():
        print('Running before calling the function')
        values = func()
        print('Running after calling the function')
        return values

    return wrapper


def say_hello():
    print('Hello from the other side')


say_hello = simple_decorator(say_hello)
say_hello()
