from multiprocessing import Pool
import time

def cube(number):
    return number**3

if __name__ == '__main__':
    start = time.time()

    # Using multiprocessing
    pool = Pool()
    numbers = range(100000)

    result = pool.map(cube, numbers)

    pool.close()
    pool.join()

    # Normal way
    # result = [i**3 for i in range(1000000)]
    end = time.time()

    # print(result)
    print('processing time', end-start)