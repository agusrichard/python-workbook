def reverse_integer(x):    
    result = 0
    if x == 0:
        return result

    s = str(abs(x))
    if x < 0:
        result = int('-' + s[::-1].lstrip('0'))
    else:
        result = int(s[::-1].lstrip('0'))

    return result if is_int32(result) else 0

def is_int32(number):
    return -1 * (2**31) <= number <= (2**31)-1



print(reverse_integer(123))
print(reverse_integer(-123))
print(reverse_integer(120))
print(reverse_integer(0))
print(reverse_integer(-10))
print(reverse_integer(1534236469))
print()
