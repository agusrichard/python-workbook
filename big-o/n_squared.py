import sys

def n_squared(n):
    total = 0
    for i in range(n):
        for j in range(n):
            print(i, j)
            total += 1

    print('TOTAL:', total)

if __name__ == '__main__':
    n_squared(int(sys.argv[1]))