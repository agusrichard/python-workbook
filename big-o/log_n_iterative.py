import sys

def log_n_iterative(n):
    while n >= 1:
        print(n)
        n = n // 2


if __name__ == '__main__':
    log_n_iterative(int(sys.argv[1]))