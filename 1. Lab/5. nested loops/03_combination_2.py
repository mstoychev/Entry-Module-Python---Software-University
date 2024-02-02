N_number = int(input())
count = 0
for x1 in range(0, N_number + 1):
    for x2 in range(0, N_number + 1):
        for x3 in range(0, N_number + 1):
            if x1 + x2 + x3 == N_number:
                count += 1
print(count)