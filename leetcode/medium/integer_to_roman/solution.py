def integer_to_roman(num: int) -> str:
    nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    result = ""
    while num:
        div = num // nums[i]
        num %= nums[i]

        while div:
            result += sym[i]
            div -= 1
        i -= 1

    return result


print(integer_to_roman(10))
print(integer_to_roman(3549))
