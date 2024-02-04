first_num = int(input())
second_num = int(input())
third_num = int(input())

for i in range(1, first_num + 1):
    a = 0
    if i % 2 == 0:
        a = i
        for j in range(1, second_num + 1):
            b = 0
            if j % 2 == 0:
                b = j
                for z in range(1, third_num + 1):
                    c = 0
                    if z % 2 == 0:
                        c = z
                        print(f"{a} {b} {c}")
