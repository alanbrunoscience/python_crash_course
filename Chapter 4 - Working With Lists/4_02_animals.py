animals = ['lion', 'cat', 'leopard']

print("*** ANIMALS NAME ***\n")

i = 0

for animal in animals:
    if animal is not animals[-1]:
        print(f"- {animal.title()};")
    else:
        print(f"- {animal.title()}.")
        

print("\n*** STATEMENT ABOUT ANIMALS ***\n")

i = 0

for animal in animals:
    if animal is not animals[-1]:
        print(f"- {animal.title()} is a feline;")
    else:
        print(f"- {animal.title()} is a feline.")
        
print("\nAll these animals are felines.")