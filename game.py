time_min = 20
time_sec = 0
# time_possesion = 0

import random


def genTimeLeft(time_minutes, time_seconds, time_possesion):
    if time_seconds - time_possesion < 0:
        time_seconds = time_seconds - time_possesion + 60
        if time_minutes > 0:
            time_minutes -= 1
        else:
            time_seconds = 0
    else:
        time_seconds -= time_possesion     
    return time_minutes, time_seconds

def display_time(minutes, seconds):
    return '{}:{}'.format(minutes, str(seconds).zfill(2))

print(display_time(time_min, time_sec))
while time_min > 0 or time_sec > 1:
    time_min, time_sec = genTimeLeft(time_min, time_sec, random.randint(1, 30))
    print(display_time(time_min, time_sec))

