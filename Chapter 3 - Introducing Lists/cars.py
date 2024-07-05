cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort() # sort list in alphabetical order (permanently)
print(cars)

cars.sort(reverse=True) # sort list in reverse-alphabetical order (permanently)
print(cars)

# -----------------------------------------------------------------------------

# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']

print(f"\nHere is the original list: {cars}")

print(f"\nHere is the sorted list: {sorted(cars)}")

print(f"\nHere is the original list again: {cars}\n")

# -----------------------------------------------------------------------------

# Printing a List in Reverse Order

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)