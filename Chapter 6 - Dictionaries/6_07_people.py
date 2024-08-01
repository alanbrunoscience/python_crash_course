person_01 = {
    'first_name': 'alan',
    'last_name': 'bruno',
    'age': 27,
    'city': 'barueri',
}

person_02 = {
    'first_name': 'ronald',
    'last_name': 'tolkien',
    'age': 45,
    'city': 'oxford',
}

person_03 = {
    'first_name': 'kezia',
    'last_name': 'batista',
    'age': 37,
    'city': 'barueri',
}

people = [person_01, person_02, person_03]

for person in people:
    print(f"First name: {person['first_name'].title()};")
    print(f"Last name: {person['last_name'].title()};")
    print(f"Age: {person['age']};")
    print(f"City: {person['city'].title()}.\n")