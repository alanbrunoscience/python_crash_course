def make_pizza(size, *toppings):
    """ Summarize the pizza we are about to make. """
    print(f"Making a {size}-inch pizza with the following toppings:\n")
    for topping in toppings:
        if topping != toppings[-1]:
            print(f"-> {topping.title()};")
        else:
            print(f"-> {topping.title()}.")
    print()