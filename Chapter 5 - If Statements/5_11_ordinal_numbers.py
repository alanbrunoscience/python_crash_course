numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print(f"{number}st", end=" ")
    elif number == 2:
        print(f"{number}nd", end=" ")
    elif number == 3:
        print(f"{number}rd", end=" ")
    elif number > 3:
        print(f"{number}th", end=" ")
    
print()