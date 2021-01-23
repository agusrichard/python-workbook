def outer_function():
    def inner_function_one():
        print("Calling first inner function")

    def inner_function_two():
        print("Calling second inner function")

    inner_function_one()
    inner_function_two()


outer_function()