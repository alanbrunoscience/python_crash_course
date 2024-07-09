my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:\n")
for food in my_foods:
    if food is not my_foods[-1]:
        print(f"- {food.title()};")
    else:
        print(f"- {food.title()}.")

print("\nMy friend's favorite foods are:\n")
for food in friend_foods:
    if food is not friend_foods[-1]:
        print(f"- {food.title()};")
    else:
        print(f"- {food.title()}.")