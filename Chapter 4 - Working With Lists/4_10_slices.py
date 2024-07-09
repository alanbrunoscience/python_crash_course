players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(f"*** ORIGINAL LIST ***\n\n{players}\n")

print(f"-> The first three items in the list are: {players[0:3]};\n") # Or players[:3]

middle = len(players) // 2

print(f"-> The items from the middle of the list are: {players[middle:]};\n")

print(f"-> The last three items on the list are: {players[-3:]}.")