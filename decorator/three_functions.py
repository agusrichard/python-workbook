# Function with one argument and returns string
def tell_me_your_age(age):
    return f"I am {age} years old."


# Function with one argument (string) and returns string
def introduce(name):
    return f"HI... My name is {name} and nice to see you!"


# Function with one function as argument and returns its value
def introduce_john(func):
    return introduce("John")


print(tell_me_your_age(10))
print(introduce("Mike"))
print(introduce_john(introduce))