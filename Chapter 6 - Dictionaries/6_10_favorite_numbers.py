favorite_numbers = {
    'alan': [1, 37, 3],
    'kezia': [2, 27, 2],
    'julia': [3, 4],
    'victoria': [4, 5],
    'duda': [5],
}

print("*** FAVORITE NUMBERS ***\n")
for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(f"{name.title()}, your favorite numbers are:\n\n>> ", end=" ")
    else:
        print(f"{name.title()}, your favorite number is:\n\n>> ", end=" ")
    for number in numbers:
        print(f"{number} ", end=" ")
    print('\n')