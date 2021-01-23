def simple_decorator(func):
    """Takes function, modifies it and returns the wrapper"""

    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")

    return wrapper


def say_hi():
    print("Hiiiii....")


say_hi = simple_decorator(say_hi)
say_hi()

# Returns:
# Before calling the function
# Hiiiii....
# After calling the function