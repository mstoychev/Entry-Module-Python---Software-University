trip = float(input())
num_puzzle = int(input())
num_doll = int(input())
teddy_num = int(input())
minion_num = int(input())
truck_num = int(input())
puzzle = 2.6
doll = 3
teddy = 4.1
minion = 8.2
truck = 2

total_sum = num_puzzle * puzzle + num_doll * doll + teddy_num * teddy + minion_num * minion + truck_num * truck
num_toys = num_puzzle + num_doll + teddy_num + minion_num + truck_num

if num_toys >= 50:
    total_sum *= 0.75

final_money = total_sum * 0.9    #aquí le resto 10% del alquiler
resto_positivo = final_money - trip
resto_negativo = trip - final_money

if final_money >= trip:
    print(f"Yes! {f'{resto_positivo:.2f}'} lv left.")
else:
    print(f"Not enough money! {f'{resto_negativo:.2f}'} lv needed.")
