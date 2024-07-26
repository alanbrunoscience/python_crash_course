# Insert elements at the end of the list
motorcycles = ["Honda", "Yamaha", "Suzuki"]
print(motorcycles)

motorcycles.append("Ducati")
print(motorcycles)

# Insert elements in any position in the list
motorcycles = ["Triumph", "Royal Enfield", "Harley-Davidson"]
print(motorcycles)

motorcycles.insert(0, "Kawasaki")
print(motorcycles)

# Removing an Item Using the del Statement
motorcycles = ["Honda", "Yamaha", "Suzuki"]
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# Removing an Item Using the pop() Method
motorcycles = ["Honda", "Yamaha", "Suzuki"]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# pop() method application
motorcycles = ["Honda", "Yamaha", "Suzuki"]

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Popping Items from Any Position in a List
motorcycles = ["honda", "yamaha", "suzuki"]

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing an Item by Value
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)

motorcycles.remove("ducati")
print(motorcycles)

# Using the remove() method to work with a value that's being removed from a list
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)

too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
