def zigzag_conversion(s, numRows):
    n = len(s)

    result = ''
    for row in range(numRows):
        skipped = 2 * (numRows-row) - 2
        ind = row
        while True:
            if ind > n:
                break
            result += s[ind]
            if skipped == -1:
                ind += 2 * numRows - 2
            else:
                ind += skipped
                
                
    return result


# P     I    N
# A   L S  I G
# Y A   H R
# P     I
print(zigzag_conversion('PAYPALISHIRING', 4))