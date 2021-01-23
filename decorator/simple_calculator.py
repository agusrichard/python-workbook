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