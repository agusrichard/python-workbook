import sys

counter = 0

def n_log_n(n):
    global counter

    y = n
    while n > 1:
        n = n // 2
        for i in range(y):
            print(i)
            counter += 1


if __name__ == '__main__':
    n_log_n(int(sys.argv[1]))
    print('Counter: ', counter)