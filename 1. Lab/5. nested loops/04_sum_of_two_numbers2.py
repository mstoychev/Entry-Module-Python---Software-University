initial_num = int(input())
final_num = int(input())
magic_num = int(input())
counter = 0
flag_found = False
for i in range(initial_num, final_num + 1):
    for j in range(initial_num, final_num + 1):
        counter += 1
        if i + j == magic_num:
            print(f"Combination N:{counter} ({i} + {j} = {magic_num})")
            flag_found = True
            break
    if flag_found:
        break
if not flag_found:
    print(f"{counter} combinations - neither equals {magic_num}")