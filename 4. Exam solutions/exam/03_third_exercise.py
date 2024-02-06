import math
cat_breed = input()
cat_sex = input()
years = 0
cat_month = 0
if cat_breed == "British Shorthair":
    if cat_sex == "m":
        years = 13
        cat_month = years * 12 / 6
        print(f"{math.ceil(cat_month)} cat months")
    elif cat_sex == "f":
        years = 14
        cat_month = years * 12 / 6
        print(f"{math.ceil(cat_month)} cat months")

elif cat_breed == "Siamese":
    if cat_sex == "m":
        years = 15
        cat_month = years * 12 / 6
        print(f"{math.ceil(cat_month)} cat months")
    elif cat_sex == "f":
        years = 16
        cat_month = years * 12 / 6
        print(f"{math.ceil(cat_month)} cat months")

elif cat_breed == "Persian":
    if cat_sex == "m":
        years = 14
        cat_month = years * 12 / 6
        print(f"{math.ceil(cat_month)} cat months")
    elif cat_sex == "f":
        years = 15
        cat_month = years * 12 / 6
        print(f"{math.ceil(cat_month)} cat months")

elif cat_breed == "Ragdoll":
    if cat_sex == "m":
        years = 16
        cat_month = years * 12 / 6
        print(f"{math.ceil(cat_month)} cat months")
    elif cat_sex == "f":
        years = 17
        cat_month = years * 12 / 6
        print(f"{math.ceil(cat_month)} cat months")

elif cat_breed == "American Shorthair":
    if cat_sex == "m":
        years = 12
        cat_month = years * 12 / 6
        print(f"{math.ceil(cat_month)} cat months")
    elif cat_sex == "f":
        years = 13
        cat_month = years * 12 / 6
        print(f"{math.ceil(cat_month)} cat months")

elif cat_breed == "Siberian":
    if cat_sex == "m":
        years = 11
        cat_month = years * 12 / 6
        print(f"{math.ceil(cat_month)} cat months")
    elif cat_sex == "f":
        years = 12
        cat_month = years * 12 / 6
        print(f"{math.ceil(cat_month)} cat months")

else:
    print(f"{cat_breed} is invalid cat!")
