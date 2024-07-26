age = 12

if age < 4:
    price = 0.00
elif age < 18:
    price = 25.00
elif age < 65:
    price = 40.00
elif age >= 65:
    price = 20.00

print(f"Your admission cost is $ {price:.2f}.")