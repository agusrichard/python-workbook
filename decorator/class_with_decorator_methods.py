import functools
import time


class MyClass:
    def __init__(self):
        self.num_calls = 0

    def timer(self, func):
        """Returns the time it takes for some function to execute"""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.num_calls += 1
            start = time.perf_counter()
            value = func(*args, **kwargs)
            end = time.perf_counter()
            interval = end - start
            print(
                f"The time function {func.__name__} took to be executed is {interval} secs"
            )
            return value

        return wrapper

    def repeats(self, num_reps=2):
        """Repeats function call as many as num_reps times"""

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                self.num_calls += 1
                for _ in range(num_reps):
                    value = func(*args, **kwargs)
                return value

            return wrapper

        return decorator


my_class = MyClass()


@my_class.timer
def say_hi():
    print("Hi!")


say_hi()


@my_class.repeats(num_reps=5)
def say_ho():
    print("Ho!")


say_ho()
print(my_class.num_calls)
