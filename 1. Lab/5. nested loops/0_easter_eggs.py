num_eggs = int(input())
red_eggs, orange_egg, blue_egg, green_egg = 0, 0, 0, 0

for i in range(num_eggs):
    type_of_egg = input()
    if type_of_egg == "red":
        red_eggs += 1
    elif type_of_egg == "orange":
        orange_egg += 1
    elif type_of_egg == "blue":
        blue_egg += 1
    elif type_of_egg == "green":
        green_egg += 1

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_egg}")
print(f"Blue eggs: {blue_egg}")
print(f"Green eggs: {green_egg}")

