city = input()
sales = float(input())
commission = 0
if city == "Sofia":
    if 0 <= sales <= 500:
        commission = 5 / 100
        print(f"{(commission * sales):.2f}")
    elif 500 < sales <= 1000:
        commission = 7 / 100
        print(f"{(commission * sales):.2f}")
    elif 1000 < sales <= 10000:
        commission = 8 / 100
        print(f"{(commission * sales):.2f}")
    elif sales > 10000:
        commission = 12 / 100
        print(f"{(commission * sales):.2f}")
    else:
        print("error")

elif city == "Varna":
    if 0 <= sales <= 500:
        commission = 4.5 / 100
        print(f"{(commission * sales):.2f}")
    elif 500 < sales <= 1000:
        commission = 7.5 / 100
        print(f"{(commission * sales):.2f}")
    elif 1000 < sales <= 10000:
        commission = 10 / 100
        print(f"{(commission * sales):.2f}")
    elif sales > 10000:
        commission = 13 / 100
        print(f"{(commission * sales):.2f}")
    else:
        print("error")

elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 5.5 / 100
        print(f"{(commission * sales):.2f}")
    elif 500 < sales <= 1000:
        commission = 8 / 100
        print(f"{(commission * sales):.2f}")
    elif 1000 < sales <= 10000:
        commission = 12 / 100
        print(f"{(commission * sales):.2f}")
    elif sales > 10000:
        commission = 14.5 / 100
        print(f"{(commission * sales):.2f}")
    else:
        print("error")
else:
    print("error")
