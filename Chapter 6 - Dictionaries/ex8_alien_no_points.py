# For dictionaries specifically, you can use the get() method to set
# a default value that will be returned if the requested key doesn’t 
# exist.

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
# point_value = alien_0.get('points') # The output in this case is 'None'.
print(point_value)