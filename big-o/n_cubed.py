import sys

def n_cubed(n):
    total = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)
                total += 1

    print('TOTAL:', total)

if __name__ == '__main__':
    n_cubed(int(sys.argv[1]))