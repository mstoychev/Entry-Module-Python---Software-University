import math
N_days = int(input())
M_kilometers = float(input())
km_goal = 1000
total_kilometers = M_kilometers

current_day_km = M_kilometers
for i in range(0, N_days):
    current_percent = int(input())
    current_day_km *= (1 + current_percent / 100)
    total_kilometers += current_day_km

diff = abs(total_kilometers - km_goal)
if total_kilometers >= km_goal:
    print(f"You've done a great job running {math.ceil(diff)} more kilometers!")
elif total_kilometers < km_goal:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(diff)} more kilometers")

