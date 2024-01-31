import sys
minimal_number = sys.maxsize
command = input()
while command != "Stop":
    current_number = int(command)
    if current_number <= minimal_number:
        minimal_number = current_number
    
    command = input()

print(minimal_number)
