budget = float(input())
N_vid = int(input())
M_process = int(input())
P_ram = int(input())
final_price = (N_vid * 250) + ((0.35 * N_vid * 250) * M_process) + ((0.1 * N_vid * 250) * P_ram)

if N_vid > M_process:
    final_price *= 0.85

if budget >= final_price:
    print(f"You have {f'{budget - final_price:.2f}'} leva left!")
else:
    print(f"Not enough money! You need {f'{final_price - budget:.2f}'} leva more!")
