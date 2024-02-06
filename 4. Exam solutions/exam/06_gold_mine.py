num_locations = int(input())

for i in range(1, num_locations + 1):
    goal_average = float(input())
    days_per_locations = int(input())
    total_kg_location = 0
    average_location = 0
    for j in range(1, days_per_locations + 1):
        current_kg = float(input())
        total_kg_location += current_kg

    average_location = total_kg_location / days_per_locations
    diff = abs(goal_average - average_location)
    if average_location >= goal_average:
        print(f"Good job! Average gold per day: {average_location:.2f}.")
    else:
        print(f"You need {diff:.2f} gold.")