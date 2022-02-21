def palindrome_number(x: int) -> bool:
    pal = str(x)
    mid = len(pal) // 2
    for i in range(mid):
        if pal[i] != pal[-(i + 1)]:
            return False

    return True
