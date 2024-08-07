prompt = "Enter an age, please (enter 0 to exit): "

age = 1

while age > 0:
    
    age = int(input(prompt))
    
    if age == 0:
        print(f"\n-> Finishing the program...")
        break
    elif age < 3:
        price = 0
    elif age < 12:
        price = 10.00
    elif age >= 12:
        price = 15.00
    
    print(f"\n-> The ticket's price is ${price:.2f}.\n")