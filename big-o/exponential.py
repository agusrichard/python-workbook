import sys

counter = 0

def fib(n):
    global counter

    if n == 0:
        counter += 1
        return 0
    if n == 1:
        counter += 1
        return 1

    return fib(n-1) + fib(n-2)

def exponential(n):
    global counter

    if n == 0:
        counter += 1
        return
    
    exponential(n-1)
    exponential(n-1)

if __name__ == '__main__':
    print('Fibonacci result:', fib(int(sys.argv[1])))
    print('Fibonacci Counter: ', counter)

    counter = 0
    exponential(int(sys.argv[1]))
    print('Exponential Counter: ', counter)