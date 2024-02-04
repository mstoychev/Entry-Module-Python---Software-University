import math
days = int(input())
available_food = int(input())
food_1_deer = float(input())
food_2_deer = float(input())
food_3_deer = float(input())
food_needed = food_1_deer * days + food_2_deer * days + food_3_deer * days
diff = abs(available_food - food_needed)
if available_food >= food_needed:
    print(f"{math.floor(diff)} kilos of food left.")
elif food_needed > available_food:
    print(f"{math.ceil(diff)} more kilos of food are needed.")
