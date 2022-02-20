def string_to_integer(s: str) -> int:
    sign = 1 
    result = 0
    index = 0
    n = len(s)
    
    INT_MAX = pow(2,31) - 1 
    INT_MIN = -pow(2,31)
    
    # Discard all spaces from the beginning of the s string.
    while index < n and s[index] == ' ':
        index += 1
    
    # sign = +1, if it's positive number, otherwise sign = -1. 
    if index < n and s[index] == '+':
        sign = 1
        index += 1
    elif index < n and s[index] == '-':
        sign = -1
        index += 1
    
    # Traverse next digits of s and stop if it is not a digit. 
    # End of string is also non-digit character.
    while index < n and s[index].isdigit():
        digit = int(s[index])
        
        # Check overflow and underflow conditions. 
        if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
            # If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.    
            return INT_MAX if sign == 1 else INT_MIN
        
        # Append current digit to the result.
        result = 10 * result + digit
        index += 1
    
    # We have formed a valid number without any overflow/underflow.
    # Return it after multiplying it with its sign.
    return sign * result



print(string_to_integer('42'))
print(string_to_integer('   -42'))
print(string_to_integer('4193 with words'))
print(string_to_integer('+-12'))
print(string_to_integer('21474836460'))
print(string_to_integer('00000-42a1234'))
print(string_to_integer('  0000000000012345678'))