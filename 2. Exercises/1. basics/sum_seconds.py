import math

fist_sport = int(input())
second_sport = int(input())
third_sport = int(input())
total_time_in_sec = fist_sport + second_sport + third_sport

hours = math.floor(total_time_in_sec / 60)
mins = total_time_in_sec % 60
if mins <=9:
    print(f"{hours}:0{mins}")
else:
    print(f"{hours}:{mins}")


