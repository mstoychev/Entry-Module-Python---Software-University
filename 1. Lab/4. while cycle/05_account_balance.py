command = input()
total = 0

while command != "NoMoreMoney":
    income = float(command)
    if income < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {income:.2f}")
    total += income
    command = input()

print(f"Total: {total:.2f}")