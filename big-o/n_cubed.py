import sys

counter = 0

def n_cubed(n):
    global counter

    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)
                counter +=1

if __name__ == '__main__':
    n_cubed(int(sys.argv[1]))
    print('Counter:', counter)