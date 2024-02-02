plants = int(input())
apartments = int(input())

for i in range(plants, 0, -1):
    current_room = ""
    if i == plants:
        i_str = str(i)
        current_room += "L" + i_str
    elif i % 2 == 0:
        i_str = str(i)
        current_room += "O" + i_str
    elif i % 2 == 1:
        i_str = str(i)
        current_room += "A" + i_str

    line_to_print = ""
    for j in range(0, apartments):
        current_room_clean = ""
        current_room_clean = current_room
        j_str = str(j)
        current_room_clean += j_str
        line_to_print += current_room_clean + " "

    print(line_to_print)