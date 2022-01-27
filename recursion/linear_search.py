from typing import List


def linear_search(lst: List, val: int) -> int:
    return linear_search_helper(lst, val, 0)


def linear_search_helper(lst: List, val: int, acc: int) -> int:
    if len(lst) == 0:
        return -1

    if acc >= len(lst):
        return -1

    if lst[acc] == val:
        return acc

    return linear_search_helper(lst, val, acc+1)



if __name__ == "__main__":
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(linear_search(lst, 20))
