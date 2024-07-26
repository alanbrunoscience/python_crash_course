# Tuples (An Immutable List)

dimensions = (200, 50)

# dimensions[0] = 250 # TypeError: 'tuple' object does not support 
# item assignment

# print(dimensions[0])
# print(dimensions[1])

for dimension in dimensions:
    print(dimension)