address_N = int(input())
address_M = int(input())
address_S = int(input())
print_line = ""

for i in range(address_M, address_N - 1, -1):
    if i % 2 == 0 and i % 3 == 0:
        if i == address_S:
            break
        i_str = str(i)
        print_line += i_str + " "

print(print_line)
