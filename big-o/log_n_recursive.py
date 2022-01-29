import sys

counter = 0

def log_n_recursive(n):
    global counter
    
    if n <= 1:
        return
    
    print(n)
    counter += 1
    log_n_recursive(n // 2)


if __name__ == '__main__':
    log_n_recursive(1024)
    print('Counter: ', counter)