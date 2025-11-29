'''
Day15: Python Date time
Today's work:
1. create date time in Python
2. draw time series use date time

'''

'''
Note Part
datetime is a module can be import

import datetime #1
import datetime from datetime #2
the two line is different:
now1 = datetime.datetime.now() #1 import the whole module
now = datetime.now() #2 import datetime part from the whole module

Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC.
'''

'''
Question Part
print(list) will give the official representation?
for example
print(time1)
2019-12-05 00:00:00
print(timeline)
[datetime.datetime(2019, 12, 5, 0, 0), datetime.datetime(2019, 12, 6, 0, 0)]
that is an interesting condition

'''

# Main Program
import datetime
# print(dir(datetime))
# now1 = datetime.datetime.now()
# print(now1)
# from datetime import datetime
now = datetime.datetime.now()
print(now)
timestamp = now.timestamp()
print('timestamp', timestamp)
after_5_days = now + datetime.timedelta(days=5)
print('after_5_days', after_5_days)

time_one = now.strftime('%m/%d/%Y, %H:%M:%S')
print('time_one', time_one)
time_two = now.strftime('%d/%m/%Y, %H:%M:%S')
print('time_two', time_two)

date_string = "5 December, 2019"
print("date_string =", date_string)
# if give no setting of format, use the default setting as yyyy-mm-dd HH:MM:SS
date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
# I think this line is best
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)

from datetime import timedelta
# timedelta will not create an exact time, just a 'delta'
# t1 = 94 days, 4:00:20
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
print("t1 =", t1)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)

# Exercise
# Time series analysis
from datetime import time, datetime
import matplotlib.pyplot as plt
date_string1 = '5 December, 2019'
date_string2 = '2019-12-06'
time1 = datetime.strptime(date_string1, "%d %B, %Y")
print("time1 =", time1)
time2 = datetime.strptime(date_string2, "%Y-%m-%d")
timeline = [time1, time2]
print("timeline =", timeline)
valueline = [1,2]
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(timeline, valueline)
# just show the 2 point
ax.set_xticks(timeline)
plt.show()


