import sys

counter = 0

def constant_time(a):
    global counter
    counter += 1

    return 0

if __name__ == '__main__':
    constant_time(int(sys.argv[1]))
    print('Counter:', counter)