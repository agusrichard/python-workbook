import numpy as np


def select(seq, start):
    min_index = start

    for i in range(min_index + 1, len(seq)):
        if seq[min_index] > seq[i]:
            min_index = i

    return min_index


def selection_sort(seq):
    for i in range(len(seq) - 1):
        min_index = select(seq, i)
        tmp = seq[i]
        seq[i] = seq[min_index]
        seq[min_index] = tmp

    return seq


if __name__ == "__main__":
    lst = np.random.randint(10, size=10)
    selection_sort(lst)
    print(lst)
