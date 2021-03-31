from multiprocessing import Process, Value, Array, Lock
import time

def add100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1


if __name__ == '__main__':
    shared_number = Value('i', 0)
    lock = Lock()

    print('Number at beginning', shared_number.value)

    p1 = Process(target=add100, args=(shared_number, lock))
    p2 = Process(target=add100, args=(shared_number, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Number at ending', shared_number.value)