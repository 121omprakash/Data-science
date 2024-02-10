#importing datetime class from datatime module
from datetime import datetime as dt
#dt.now() --> returns the current time along with date
print('Current time is: {}'.format(dt.now()))
#date classs that only print the date
from datetime import date as dt
#using today() method for today date
print('Today is: {}'.format(dt.today()))
#using time class

# from datetime import time as tm
# #using now() --> print current time
# print(tm.now())


#formatting and parsing the datatime

ct = dt.now()
lst = []
for i in range(1,100000000):
    lst.append(i)
tn = dt.now()
print('Total Spend time: {}'.format(tn-ct))
print(lst[-1])
tn = dt.now()
print('Total Spend time: {}'.format(tn-ct))