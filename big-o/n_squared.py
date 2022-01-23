import sys

counter = 0

def n_squared(n):
    global counter
    for i in range(n):
        for j in range(n):
            print(i, j)
            counter += 1

    print('Counter:', counter)

if __name__ == '__main__':
    n_squared(int(sys.argv[1]))