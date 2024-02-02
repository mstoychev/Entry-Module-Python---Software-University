initial_number = int(input())
final_number = int(input())
magic_number = int(input())
combination = 0
combination_found = False
for x in range(initial_number, final_number + 1):
    for y in range(initial_number, final_number + 1):
        combination += 1
        if x + y == magic_number:
            print(f"Combination N:{combination} ({x} + {y} = {magic_number})")
            combination_found = True
            break
    if combination_found:
        break
if not combination_found:
    print(f"{combination} combinations - neither equals {magic_number}")