destination = input()
savings = 0
while destination != "End":
    budget = float(input())

    while savings <= budget:
        current_save = float(input())
        savings += current_save

    print(f"Going to {destination}!")
    savings = 0
    destination = input()
