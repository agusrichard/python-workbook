class Time(object):
    """Represents the time of day
    Attributes: day,hour, minute, second"""

    def __init__(self,day=0, hour=0, minute=0, second=0):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%2d:%2d:%2d:%2d' % (self.day,self.hour,self.minute,self.second)

    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)


    def print_time(self):
        print('%2d:%2d:%2d:%2d' % (self.day,self.hour,self.minute,self.second))

    def time_to_int(self):
        hours = self.day * 24 + self.hour
        minutes = hours * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self,seconds):
        seconds = self.time_to_int() + seconds
        return int_to_time(seconds)

def int_to_time(seconds):
    timey = Time()
    minutes,timey.second = divmod(seconds,60)
    hour,timey.minute = divmod(minutes,60)
    timey.day,timey.hour = divmod(hour,24)
    return timey


time = Time(6,33,54,45)
duration = Time(9,32,30,35)
start = Time(8,32,34,53)

print(sum([time,duration,start]))



