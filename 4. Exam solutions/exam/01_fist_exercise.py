import math
num_painting = int(input())
num_roll = int(input())
price_gloves = float(input())
price_brush = float(input())

total_painting = num_painting * 21.5
total_rolls = num_roll * 5.2
num_gloves = math.ceil(0.35 * num_roll)
num_brush = math.floor(0.48 * num_painting)
total_gloves = num_gloves * price_gloves
total_brush = num_brush * price_brush
delivery = 1/15 * (total_painting + total_rolls + total_gloves + total_brush)
print(f"This delivery will cost {delivery:.2f} lv.")

