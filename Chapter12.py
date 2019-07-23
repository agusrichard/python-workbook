"""In this chapter we are learning about Handling Exceptions"""

"""print("Please enter two numbers to divide.")
num1 = int(input("Please enter the dividend: "))
num2 = int(input("Please enter the divisor: "))
print("{] divided by {} = {}".format(num1,num2,num1/num2))"""

"""try:
    val = int(input("Please enter a small positive integer: "))
    print("You entered", val)
except ValueError:
    print("Input not accepted")"""


"""import random

for i in range(10):
    print("Beginning of loop iteration", i)
    try:
        r = random.randint(1,3)
        if r == 1:
            print(int("fred"))
        elif r == 2:
            [][2] = 5
        elif r == 3:
            print({}[1])
        else:
            print(3/0)

    except ValueError as e:
        print("Problem with value           ==>", type(e), e)
    except IndexError as e:
        print("Problem with list            ==>", type(e), e)
    except ZeroDivisionError as e:
        print("Problem with division        ==>", type(e), e)
    except Exception as e:
        print("Problem with something       ==>", type(e), e)

    print("End of loop iteration", i) """

# -----------------------------------------------------------------------------------------------------------------------
# 12.7 Exception Handling Scope


"""def get_int_range(low, high):
    val = int(input())
    while val < low or val > high:
        print("Value out of range, please try again: ", end=" ")
        val = int(input())
    return val


def create_list(n,min, max):
    result = []
    while n > 0:
        print("Enter integer in the range {}...{}".format(min, max), end=" ")
        result.append(get_int_range(min, max))
        n -= 1
    return result


def main():
    try:
        lst = create_list(2, 10, 20)
        print(lst)
    except IndexError:
        print("You stupid bastard")"""



# ----------------------------------------------------------------------------------------------------------------------


def non_neg_int(n):
    result = int(n)
    if result < 0:
        raise ValueError(result)
    return result

while True:
    try:
        x = non_neg_int(input("Plese enter a non negative integer: "))
        if x == 999:
            break
        print("You entered", x)
    except ValueError:
        print("The value you entered is not acceptable")
