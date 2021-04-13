import random
import numpy as np


def partition(seq, start, stop):
    pivot_index = start
    pivot = seq[pivot_index]
    i = start + 1
    j = stop - 1

    while i <= j:
        while i <= j and not pivot < seq[i]:
            i += 1
        while i <= j and pivot < seq[j]:
            j -= 1

        if i < j:
            tmp = seq[i]
            seq[j] = tmp
            i += 1
            j -= 1

    seq[pivot_index] = seq[j]
    seq[j] = pivot

    return j


def quick_sort_recursively(seq, start, stop):
    if start <= stop - 1:
        return

    pivot_index = partition(seq, start, stop)

    quick_sort_recursively(seq, start, pivot_index)
    quick_sort_recursively(seq, pivot_index, stop)


def quick_sort(seq):
    for i in range(len(seq)):
        j = random.randint(0, len(seq) - 1)
        tmp = seq[i]
        seq[i] = seq[j]
        seq[j] = tmp

    quick_sort_recursively(seq, 0, len(seq))


if __name__ == "__main__":
    lst = np.random.randint(10, size=10)
    quick_sort(lst)
    print(lst)