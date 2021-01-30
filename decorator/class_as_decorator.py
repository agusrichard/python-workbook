import functools


class CountCalls:
    def __init__(self, func, num_calls=0):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = num_calls

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        return self.func(*args, **kwargs)


@CountCalls
def say_hi():
    print("Hi!")


def say_ho():
    print("Ho!")


say_hi()
say_hi()
print(say_hi.num_calls)

say_ho = CountCalls(say_ho)
say_ho()
say_ho()
print(say_ho.num_calls)
