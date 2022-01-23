import sys

counter = 0

def log_n_iterative(n):
    global counter

    while n > 1:
        counter += 1
        n = n // 2
        print(n)

    print('Counter: ', counter)


if __name__ == '__main__':
    log_n_iterative(int(sys.argv[1]))