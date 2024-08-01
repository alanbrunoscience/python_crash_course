# Sometimes you’ll want to store multiple dictionaries in a list, or a list of
# items as a value in a dictionary. This is called nesting. You can nest 
# dictionaries inside a list, a list of items inside a dictionary, or even a 
# dictionary inside another dictionary.

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)