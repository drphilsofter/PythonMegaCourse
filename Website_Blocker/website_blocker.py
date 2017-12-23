## block some dumb websites that are distracting

# the first thing I tried was an if statement:
# # assign the current system time, as of running this script, to the variable 'now'
# now = datetime.datetime.now()
# 
# # convert the current 'time since epoch' (in 'now') to 24 hour format, and store in variable the_time
# the_time = now.strftime('%X')
# the_time = int(the_time.replace(':', ''))
# if the_time >= 80000 and the_time <= 170000:

# the problem with this = converted time into a string, then int, and
# it no longer had connection to being a dt object, so would just behave like a 
# regular int. was fine for the one if statement comparision, but not for further use

# import the datetime module 
from datetime import datetime as dt
import time

host_path = '/etc/hosts'
host_path_temp = 'hosts' # was using for testing
redirect = '127.0.0.1'
websites = ['www.facebook.com', 'facebook.com', 'www.reddit.com', 'reddit.com', 'www.youtube.com', 'youtube.com']

# a while loop that will run continuously
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 12) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 13):
        with open(host_path, 'r+') as file:
            content = file.read()
            file.write('\n\n')
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
        print("You should be studying")
        
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
        print('You can look at those websites if you like')
    
    time.sleep(5)
    
# CRONTAB

# env EDITOR=nano crontab -e

# http://www.techradar.com/how-to/computing/apple/terminal-101-creating-cron-jobs-1305651

