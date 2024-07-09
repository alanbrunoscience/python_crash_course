cubes = []

for number in range(1, 11):
    cubes.append(number ** 3)

i = 1

for value in cubes:
    print(f'{i} ** 3 = {value}')
    i = i + 1