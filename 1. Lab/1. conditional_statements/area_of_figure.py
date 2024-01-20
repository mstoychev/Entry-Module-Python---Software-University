import math
name = input()
area = 0
if name == "square":
    a = float(input())
    area = a * a
    print(f"{area:.3f}")          #formatear con 3 ceros
elif name == "rectangle":
    a = float(input())
    b = float(input())
    area = a*b
    print(f"{area:.3f}")
elif name == "circle":
    a = float(input())
    area = math.pi * math.pow(a, 2)
    print(f"{area:.3f}")
else:
    a = float(input())
    b = float(input())
    area = a * b / 2
    print(f"{area:.3f}")
