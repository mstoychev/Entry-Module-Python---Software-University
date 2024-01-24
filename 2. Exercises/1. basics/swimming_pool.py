import math

record_in_sec = float(input())
distance_in_m = float(input())
time_per_m = float(input())
#: съпротивлението на водата го забавя на всеки 15 м. с 12.5 сек
ivans_time = (distance_in_m * time_per_m) + (math.floor(distance_in_m / 15) * 12.5)

if ivans_time >= record_in_sec:
    print(f"No, he failed! He was {f'{ivans_time - record_in_sec:.2f}'} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {f'{ivans_time:.2f}'} seconds.")
