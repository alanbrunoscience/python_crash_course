# Copying a List

my_foods = ['pizza', 'falafel', 'carrot cake']

# This doesn't work:
# friend_foods = my_foods

# Note: This syntax actually tells Python to associate the new variable friend_foods with the list that is already associated with my_foods, so now both variables point to the same list

# The correct way
friend_foods = my_foods[:] # Copying the entire original list [:] using a slice

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)