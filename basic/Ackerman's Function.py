m = int(input(">"))
n = int(input(">"))
# defining ackerman's function

def naive_ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return naive_ackermann(m - 1, 1)
    else:
        return naive_ackermann(m - 1, naive_ackermann(m, n - 1))

print(naive_ackermann(m,n))