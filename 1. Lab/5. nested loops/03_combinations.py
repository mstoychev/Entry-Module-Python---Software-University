max_number = int(input())
combinations = 0
for i in range(max_number + 1):
    for x in range(max_number + 1):
        for y in range(max_number + 1):
            if i + x + y == max_number:
                combinations += 1
print(combinations)

