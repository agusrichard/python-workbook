def do_ten_times(func):
    """Repeats func ten times"""

    def wrapper():
        for i in range(10):
            func()

    return wrapper


@do_ten_times
def say_hi():
    print("Hiiiii....")


def introduce_myself(name):
    print(f"Hi, my name is {name}")


print(say_hi.__name__)
# Returns: wrapper
print(introduce_myself.__name__)
# Return: introduce_myself