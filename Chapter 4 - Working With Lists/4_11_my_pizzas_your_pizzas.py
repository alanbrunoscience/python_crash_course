my_pizzas = ['cheese', 'chicken', 'portuguesa']
friend_pizzas = my_pizzas[:]

my_pizzas.append('margherita')
friend_pizzas.append('tuna')

print("My favorite pizzas are:\n")

for pizza in my_pizzas:
    if pizza is not my_pizzas[-1]:
        print(f"- {pizza.title()};")
    else:
        print(f"- {pizza.title()}.")
        
print("\nMy friend’s favorite pizzas are:\n")

for pizza in friend_pizzas:
    if pizza is not friend_pizzas[-1]:
        print(f"- {pizza.title()};")
    else:
        print(f"- {pizza.title()}.")