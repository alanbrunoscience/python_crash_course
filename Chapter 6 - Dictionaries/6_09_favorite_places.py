favorite_places = {
    'alan': ['united states', 'south korea', 'england'],
    'kezia': ['portugal', 'new zeland', 'italy'],
    'victoria': ['japan'],
}

for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"{name.title()}'s favorite places are:\n")
    else:
        print(f"{name.title()}'s favorite place is:\n")
    for place in places:
        if place != places[-1]:
            print(f"-> {place.title()};")
        else:
            print(f"-> {place.title()}.")
    print()