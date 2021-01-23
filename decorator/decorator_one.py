# Example of simple function which takes argument, returns value, and having side effect
def greet_repeatedly(num_times):
    for i in range(num_times):
        print("Hii")
    return "Hi, It's nice to see you!"


# Function with no argument and returns int
def tell_me_your_age(age):
    return f"I am {age} years old."


# Function with one argument (string) and returns string
def introduce(name):
    return f"HI... My name is {name} and nice to see you!"


# Function with
def introduce_john(func):
    return introduce("John")


# Parent function with two inner function
def outer_function():
    def inner_function_one():
        print("Calling first inner function")

    def inner_function_two():
        print("Calling second inner function")

    inner_function_one()
    inner_function_two()


# Simple calculator function with limited funcionalities
def simple_calculator(operation):
    """Returns operation we want, either add, subtract, multiply or divide"""

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y

    if operation == "add":
        return add
    elif operation == "subtract":
        return subtract
    elif operation == "multiply":
        return multiply
    elif operation == "divide":
        return divide
    else:
        raise Exception("Must be either add, subtract, multiply, or divide")


if __name__ == "__main__":
    addition = simple_calculator("here")
    print(addition(1, 2))
