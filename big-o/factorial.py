import sys

counter = 0

def factorial(n):
    global counter

    if n == 0:
        counter += 1
        return

    for i in range(n):
        factorial(n-1)

if __name__ == '__main__':
    factorial(int(sys.argv[1]))
    print('Counter: ', counter)