text = input()
result_sum = 0
for i in range(0, len(text)):
    character = text[i]
    if character == "a":
        result_sum += 1
    elif character == "e":
        result_sum += 2
    elif character == "i":
        result_sum += 3
    elif character == "o":
        result_sum += 4
    elif character == "u":
        result_sum += 5

print(result_sum)
