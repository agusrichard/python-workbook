# -*- coding: utf-8 -*
import datetime
import random
import time

def main():
    with open('ListAccessTiming.xml', 'wb') as file:
        file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
        file.write('<Plot title="Average List Element Access Time">\n')

        xmin = 1000
        xmax = 200000

        xList, yList = [], []

        for x in range(xmin, xmax+1, 1000):
            xList.append(x)
            prod = 0

        # Creates a list of size x with all 0’s
        lst = [0] * x
        # let any garbage collection/memory allocation complete or at least
        # settle down
        time.sleep(1)
        # Time before the 1000 test retrievals
        starttime = datetime.datetime.now()

        for v in range(1000):
            # Find a random location within the list
            # and retrieve a value. Do a dummy operation
            # with that value to ensure it is really retrieved.
            index = random.randint(0,x-1)
            val = lst[index]
            prod = prod * val
        # Time after the 1000 test retrievals
        endtime = datetime.datetime.now()

        # The difference in time between start and end.
        deltaT = endtime - starttime

        # Divide by 1000 for the average access time
        # But also multiply by 1000000 for microseconds.
        accessTime = deltaT.total_seconds() * 1000

        yList.append(accessTime)