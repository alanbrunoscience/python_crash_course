# Slicing a List

players = ['charles', 'martina', 'michael', 'florence', 'eli']

# print(players[0:3]) # ['charles', 'martina', 'michael']

# print(players[1:4]) # ['martina', 'michael', 'florence']

# print(players[:4]) # If you omit the first index in a slice, Python 
# automatically starts your slice at the beginning of the list. 
# So, the output is ['charles', 'martina', 'michael', 'florence']

# print(players[2:]) # It starts from the third item (index 2) to the 
# last item. So the output is ['michael', 'florence', 'eli']

# print(players[-3:]) # The last three players. So, ['michael', 
# 'florence', 'eli']

# Note: You can include a third value in the brackets indicating a slice. 
# If a third value is included, this tells Python how many items to skip 
# between items in the specified range.

print(players[-3::2])