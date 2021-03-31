from multiprocessing import Process, Value, Array, Lock
import time

def add100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1


if __name__ == '__main__':
    shared_numbers = Array('d', [0, 100, 200, 300])
    lock = Lock()

    print('Array at beginning', shared_numbers[:])

    p1 = Process(target=add100, args=(shared_numbers, lock))
    p2 = Process(target=add100, args=(shared_numbers, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Array at ending', shared_numbers[:])