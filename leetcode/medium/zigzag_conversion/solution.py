def zigzag_conversion(s, numRows):
    n = len(s)

    store = [[] for _ in range(numRows)]
    is_move_down = True
    row = 0
    for i in s:
        store[row] += [i]
        if is_move_down:
            row += 1
        else:
            row -= 1

        if row == 0:
            is_move_down = True

        if row == numRows-1:
            is_move_down = False

    flatened = [''.join(x) for x in store]
    return ''.join(flatened)


# P     I    N
# A   L S  I G
# Y A   H R
# P     I
print(zigzag_conversion('PAYPALISHIRING', 4))