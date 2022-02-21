def roman_to_integer(s: str) -> int:
    memo = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    agg = 0
    i = 0
    while i < len(s):
        if i == len(s) - 1:
            agg = agg + memo[s[i]]
            break
        if s[i] + s[i + 1] == "IV":
            agg = agg + 4
            i += 2
        elif s[i] + s[i + 1] == "IX":
            agg = agg + 9
            i += 2
        elif s[i] + s[i + 1] == "XL":
            agg = agg + 40
            i += 2
        elif s[i] + s[i + 1] == "XC":
            agg = agg + 90
            i += 2
        elif s[i] + s[i + 1] == "CD":
            agg = agg + 400
            i += 2
        elif s[i] + s[i + 1] == "CM":
            agg = agg + 900
            i += 2
        else:
            agg = agg + memo[s[i]]
            i += 1

    return agg
