import sys

def log_n_recursive(n):
    print(n)
    if n <= 1:
        return
    
    log_n_recursive(n // 2)


if __name__ == '__main__':
    log_n_recursive(int(sys.argv[1]))