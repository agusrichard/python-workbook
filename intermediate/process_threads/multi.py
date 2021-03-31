# from multiprocessing import Process
# import os
# import time

# processes = []
# num_processes = os.cpu_count()

# def square_numbers(num_times):
#     for i in range(num_times):
#         i * i
#         time.sleep(0.1)

# for i in range(num_processes):
#     p = Process(target=square_numbers, args=(100,))
#     processes.append(p)

# for p in processes:
#     p.start()

# for p in processes:
#     p.join()


# print('end main')

from threading import Thread
import os
import time


def square_numbers(num_times):
    for i in range(num_times):
        i * i
        time.sleep(0.2)

threads = []
num_threads = 10

for i in range(num_threads):
    t = Thread(target=square_numbers, args=(100,))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print('main ended')