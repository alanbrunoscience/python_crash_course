# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:\n")

for topping in pizza['toppings']:
    print(f"-> {topping.title()}")

print("")