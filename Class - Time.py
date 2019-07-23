class Time(object):
    """Represents the time of day
    
    Attributes: hour, minute, second"""

time = Time()
time.hour = 11
time.minute= 59
time.second = 30

duration = Time()
duration.hour = 17
duration.minute = 43
duration.second = 55

def print_time(timey):
    print('%2d:%2d:%2d:%2d' % (timey.day,timey.hour,timey.minute,timey.second))

def add_time1(time1,time2):
    sum = Time()
    sum.hour = time1.hour + time2.hour
    sum.minute = time1.minute + time2.minute
    sum.second = time1.second + time2.second
    sum.day = 0

    if sum.hour >= 24:
        sum.hour = sum.hour - 24
        sum.day += 1
    if sum.minute >= 60:
        sum.minute = sum.minute - 60
        sum.hour += 1
    if sum.second >= 60:
        sum.second = sum.second - 60
        sum.minute += 1
    return sum

def increment1(timey, seconds):
    timey.second += seconds
    if timey.second >= 60:
        timey.second -= 60
        timey.minute += 1
    if timey.minute >= 60:
        timey.minute -= 60
        timey.hour += 1
    return timey

def time_to_int(timey):
    minutes = timey.hour * 60 + timey.minute
    seconds = minutes*60 + timey.second
    return seconds

def int_to_time(seconds):
    timey = Time()
    minutes,timey.second = divmod(seconds,60)
    hour,timey.minute = divmod(minutes,60)
    timey.day,timey.hour = divmod(hour,24)
    return timey

def add_time2(t1,t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def increment2(timey,seconds):
    seconds = time_to_int(timey) + seconds
    return int_to_time(seconds)
