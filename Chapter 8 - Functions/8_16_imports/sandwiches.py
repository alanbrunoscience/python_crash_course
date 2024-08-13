def make_sandwich(*items):
    print("Making a sandwich with the following items:\n")
    for item in items:
        if item != items[-1]:
            print(f"-> {item.title()};")
        else:
            print(f"-> {item.title()}.")
    print()