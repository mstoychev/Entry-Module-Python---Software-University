first_num_max = int(input())
second_num_max = int(input())
third_num_max = int(input())
is_prime = True


for i in range(1, first_num_max + 1):
    possible_PIN = ""
    if i % 2 == 0:
        i_str = str(i)
        possible_PIN += i_str
        for x in range(1, second_num_max + 1):
            if x == 4 or x == 6 or x == 8 or x == 9:
                is_prime = False
                continue
            elif x == 2 or x == 3 or x == 5 or x == 7:
                x_str = str(x)
                if len(possible_PIN) > 1:
                    possible_PIN = int(possible_PIN)
                    possible_PIN_number = possible_PIN % 10
                    possible_PIN = str(possible_PIN_number)
                possible_PIN += " " + x_str
                for j in range(1, third_num_max + 1):
                    if j % 2 == 0:
                        possible_PIN_for_print = ""
                        j_str = str(j)
                        possible_PIN_for_print += possible_PIN + j_str
                        print(possible_PIN_for_print)
