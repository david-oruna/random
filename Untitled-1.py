#Objective: Write a Python script that reads a log file 
#containing timestamped events and calculates the time difference between the first and last entries in the log. 
#Additionally, it should display the number of unique dates on which events occurred.

import datetime

with open('events.log.yaml', 'r') as file:
    # reading the file
    log = file.read()


# extracting the timestamp of each log entry and converting it to a datetime object
# splitting the log into lines
lines = log.split('\n')
# parsing the timestamp from each line
timestamps = [line.split(' ')[0] for line in lines]
# converting the timestamps to datetime objects
dates = []


for ts in timestamps:
    try:
        m = datetime.datetime.strptime(ts, '%Y-%m-%d')
        dates.append(m)
    except ValueError:
        pass

# calculating the time difference between the first and last log entries
# finding the time difference between the first and last dates
time_diff = dates[-1] - dates[0]
# counting the number of unique dates present in the log file

unique_dates = len(set(dates))

#output

print("Time diff", time_diff)
print("Unique dates", unique_dates)