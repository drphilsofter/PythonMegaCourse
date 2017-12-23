# naming a file the current date, 
# difference between two dates

# two modules for date and time
# - time (used mostly to control time when script runs)
# - datetime

# takes time from computer time

# import datetime
# 
# now = datetime.datetime.now()
# yesterday = datetime.datetime(2017, 6, 1, 7, 12, 15, 0)
# difference = now - yesterday
# print(difference.total_seconds())

# make a file with the current date as the filename

import datetime, time

now = datetime.datetime.now()

# All of this is dumb and overly messy
# year = str(filename.year)
# month = str(filename.month)
# day = str(filename.day)
# hour = str(filename.hour)
# minute = str(filename.minute)
# second = str(filename.second)
# 
# filename = day + '-' + month + '-' + year

# http://strftime.org/

filename = now.strftime("%d-%m-%Y")
filecontents = now.strftime("%X")

def create_file():
    with open(filename + ".txt", 'w') as file:
        file.write("This process was run at " + filecontents)

create_file()


timecodes = []

for i in range(10):
    timecodes.append(datetime.datetime.now())
    time.sleep(1)

print(timecodes)







