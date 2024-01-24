hour = int(input())
minute = int(input())
total_time_min = (hour * 60) + minute + 15
final_hours = total_time_min // 60
final_minutes = total_time_min % 60

if final_hours <= 23:
    final_hours = final_hours
else:
    final_hours = "0"

if final_minutes <= 9:
    final_minutes = f"0{final_minutes}"
else:
    final_minutes = final_minutes

print(f"{final_hours}:{final_minutes}")



