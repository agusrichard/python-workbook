import sys

counter = 0

def n(a):
    global counter
    for i in range(a):
        print(i)
        counter += 1
        

if __name__ == '__main__':
    n(int(sys.argv[1]))
    print('Counter:', counter)