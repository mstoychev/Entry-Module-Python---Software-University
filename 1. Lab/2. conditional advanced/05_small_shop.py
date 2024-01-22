article = input()
city = input()
quantity = float(input())
price = 0

if city == "Sofia":
    if article == "coffee":
        price = 0.50
        money = quantity * price
        print(money)
    elif article == "water":
        price = 0.80
        money = quantity * price
        print(money)
    elif article == "beer":
        price = 1.20
        money = quantity * price
        print(money)
    elif article == "sweets":
        price = 1.45
        money = quantity * price
        print(money)
    elif article == "peanuts":
        price = 1.60
        money = quantity * price
        print(money)
elif city == "Plovdiv":
    if article == "coffee":
        price = 0.40
        money = quantity * price
        print(money)
    elif article == "water":
        price = 0.70
        money = quantity * price
        print(money)
    elif article == "beer":
        price = 1.15
        money = quantity * price
        print(money)
    elif article == "sweets":
        price = 1.30
        money = quantity * price
        print(money)
    elif article == "peanuts":
        price = 1.50
        money = quantity * price
        print(money)
elif city == "Varna":
    if article == "coffee":
        price = 0.45
        money = quantity * price
        print(money)
    elif article == "water":
        price = 0.70
        money = quantity * price
        print(money)
    elif article == "beer":
        price = 1.10
        money = quantity * price
        print(money)
    elif article == "sweets":
        price = 1.35
        money = quantity * price
        print(money)
    elif article == "peanuts":
        price = 1.55
        money = quantity * price
        print(money)

