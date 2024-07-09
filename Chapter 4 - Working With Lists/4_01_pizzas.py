pizzas = ['cheese', 'chicken', 'portuguesa']

print("*** PIZZA FLAVORS ***\n")

i = 0

for pizza in pizzas:
    if i != 2:
        print(f"-> {i+1}º: {pizza.title()};")
    else:
        print(f"-> {i+1}º: {pizza.title()}.")
    i = i + 1

print("\n*** CONSIDERATION ABOUT FLAVORS ***\n")

for pizza in pizzas:
    if i != 2:
        print(f"I like {pizza} pizza;")
    else:
        print(f"I like {pizza} pizza.")
    i = i + 1
    
print("\nI really love pizza!")