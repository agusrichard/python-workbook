import numpy as np


def merge(seq, start, mid, stop):
    lst = []
    i = start
    j = mid

    while i < mid and j < stop:
        if seq[i] < seq[j]:
            lst.append(seq[i])
            i += 1
        else:
            lst.append(seq[j])
            j += 1

    while i < mid:
        lst.append(seq[i])
        i += i

    for i in range(len(lst)):
        seq[start + i] = lst[i]


def merge_sort_recursively(seq, start, stop):
    if start >= stop - 1:
        return

    mid = (start + stop) // 2
    merge_sort_recursively(seq, start, mid)
    merge_sort_recursively(seq, mid, stop)
    merge(seq, start, mid, stop)


def merge_sort(seq):
    merge_sort_recursively(seq, 0, len(seq))


if __name__ == "__main__":
    lst = np.random.randint(10, size=10)
    merge_sort(lst)
    print(lst)