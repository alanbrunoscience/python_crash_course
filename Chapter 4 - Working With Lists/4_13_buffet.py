foods = ('carrot', 'potato', 'chicken', 'salmon', 'cheese')

print("Restaurant food offerings:\n")
for food in foods:
    if food is not foods[-1]:
        print(f"- {food.title()};")
    else:
        print(f"- {food.title()}.")
        

# Trying to modify an element
# foods[0] = 'eggs'

foods = ('beef', 'quinoa', 'chicken', 'salmon', 'cheese')

print("\nNew restaurant food offerings:\n")
for food in foods:
    if food is not foods[-1]:
        print(f"- {food.title()};")
    else:
        print(f"- {food.title()}.")