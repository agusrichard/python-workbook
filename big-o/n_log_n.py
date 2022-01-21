import sys

def n_log_n(n):
    y = n
    while n > 1:
        n = n // 2
        for i in range(y):
            print(i)


if __name__ == '__main__':
    n_log_n(int(sys.argv[1]))