from threading import Thread, Lock, current_thread
from queue import Queue
import time

def worker(q, lock):
    while True:
        value = q.get()
        with lock:
            print(f'{current_thread().name} got {value}')
        q.task_done()

if __name__ == '__main__':
    q = Queue()
    lock = Lock()

    num_threads = 10
    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True        # this thread will die after then main thread dies
                                    # if this is false, this daemon thread won't exit after the main thread is done
        thread.start()
    
    print('here')

    for i in range(1, 21):
        q.put(i)

    q.join()

    print('end main thread')