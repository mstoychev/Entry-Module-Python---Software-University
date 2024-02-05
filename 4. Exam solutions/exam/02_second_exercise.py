import math
name = input()
budget = float(input())
num_beer = int(input())
num_chips = int(input())


total_beer = 1.2 * num_beer
price_chips = 0.45 * total_beer
total_chips = math.ceil(price_chips * num_chips)
total_sum = total_beer + total_chips
diff = abs(budget - total_sum)
if budget >= total_sum:
    print(f"{name} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{name} needs {diff:.2f} more leva!")