import datetime

# Use the correct filename
filename = 'events.log'

# Initialize a list to hold the datetime objects
datetime_objects = []

with open(filename, 'r') as file:
    for line in file:
        # Extract the full datetime string from each line
        timestamp_str = line.split(' ', 1)[0] + ' ' + line.split(' ')[1]
        # Convert the string to a datetime object
        datetime_obj = datetime.datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
        datetime_objects.append(datetime_obj)

# Calculate the time difference between the first and last entries
time_diff = datetime_objects[-1] - datetime_objects[0]

# Extract just the date part for each datetime object to count unique dates
unique_dates = len(set([dt.date() for dt in datetime_objects]))

# Output the results
print(f"Time difference between first and last log entry: {time_diff}")
print(f"Number of unique dates: {unique_dates}")
