floors = int(input())
apartments = int(input())
combination = ""
print_line = ""
letter = ""

for i in range(floors, 0, -1):
    print_line = ""
    combination = ""
    if i == floors:
        combination = "L"
    elif i % 2 == 0:
        combination = "O"
    else:
        combination = "A"
    i_str = str(i)
    combination += i_str
    for j in range(apartments):
        j_str = str(j)
        combination_ok = combination
        combination_ok += j_str
        print_line += combination_ok + " "

    print(print_line)

