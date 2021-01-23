def simple_decorator(func):
    """Takes function, modifies it and returns the wrapper"""

    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")

    return wrapper


@simple_decorator
def say_ho():
    print("Hoo?")


say_ho()

# Returns
# Before calling the function
# Hoo?
# After calling the function