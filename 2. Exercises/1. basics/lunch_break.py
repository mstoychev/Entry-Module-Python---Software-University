import math

serial_name = input()
time_episode = int(input())
time_rest = int(input())
lunch_time = 0.125 * time_rest
free_time = 0.25 * time_rest
my_time = time_rest - lunch_time - free_time

if my_time >= time_episode:
    print(f"You have enough time to watch {serial_name} and left with {math.ceil(my_time - time_episode)} "
          f"minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(time_episode - my_time)} "
          f"more minutes.")
