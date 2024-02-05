base = 5364
everest_peak = 8848
day = 1
goal_reached = False

meters_climbed = base
while True:
    current_command = input()
    if current_command == "END":
        break
    current_meters = int(input())
    meters_climbed += current_meters

    if current_command == "Yes":
        day += 1
        if day == 5:
            break

    if meters_climbed >= everest_peak:
        goal_reached = True
        break

if goal_reached:
    print(f"Goal reached for {day} days!")
else:
    print("Failed!")
    print(f"{meters_climbed}")
