from datetime import datetime, timedelta, timezone

# Replace these values with the desired IST time
hour = 15
min = 35

# Create a datetime object with the given hour and minute in IST time zone
ist_time = datetime(1, 1, 1, hour, min)

# Calculate the time difference between UTC and IST time zones
time_difference = timedelta(hours=5, minutes=30)

# Convert the IST time to UTC time by subtracting the time difference
utc_time = ist_time - time_difference

# Extract the hour and minute from the UTC time
utc_hour = utc_time.hour
utc_min = utc_time.minute

print(f"The given IST time of {hour}:{min} is equivalent to {utc_hour}:{utc_min} in UTC time zone.")
