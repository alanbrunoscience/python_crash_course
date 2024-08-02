number = input("Enter a number, please: ")

number = int(number)

if number % 10 == 0:
    print(f"\n{number} is multiple of 10.")
else:
    print(f"\n{number} is not multiple of 10.")