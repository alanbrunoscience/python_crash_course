favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people = ['jen', 'sarah', 'alan', 'kezia', 'bruno']

for person in people:
    if person in favorite_languages.keys():
        print(f"{person.title()}, thanks for taking the poll.")
    else:
        print(f"{person.title()}, you haven't participated in the poll " +
              "yet. Respond it, please.")