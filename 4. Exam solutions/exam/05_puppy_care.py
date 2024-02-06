bought_food = int(input()) * 1000
total_food = 0

current_command = input()
while current_command != "Adopted":
    current_grams = int(current_command)
    total_food += current_grams

    current_command = input()

diff = abs(bought_food - total_food)
if bought_food >= total_food:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
