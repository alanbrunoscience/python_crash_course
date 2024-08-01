pet_01 = {'kind':'dog', 'owner_name': 'alan'}
pet_02 = {'kind':'hamster', 'owner_name': 'kezia'}
pet_03 = {'kind':'cat', 'owner_name': 'gabriela'}
pet_04 = {'kind':'horse', 'owner_name': 'vincenzo'}
pet_05 = {'kind':'parrot', 'owner_name': 'bia'}

pets = [pet_01, pet_02, pet_03, pet_04, pet_05]

for pet in pets:
    print(f"Kind of animal: {pet['kind'].title()};")
    if pet != pets[-1]:
        print(f"Owner's name: {pet['owner_name'].title()}.\n")
    else:
        print(f"Owner's name: {pet['owner_name'].title()}.")