budget = float(input())
num_stats = int(input())
clothes_per_stat = float(input())
decoration = 0.1 * budget

if num_stats <= 150:
    total_clothes = num_stats * clothes_per_stat
else:
    total_clothes = 0.9 * (num_stats * clothes_per_stat)

final_price = total_clothes + decoration

if final_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {f'{(final_price - budget):.2f}'} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {f'{(budget - final_price):.2f}'} leva left.")
