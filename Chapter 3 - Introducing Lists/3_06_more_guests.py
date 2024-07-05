guests_list = ["jesus", "jean", "crisely"]

print(f"{guests_list[0].title()}, {guests_list[1].title()}, and {guests_list[2].title()} I found a bigger table for the dinner. So, I'll invite more guests.\n")

guests_list.insert(0, "eusebio")
print(guests_list)

middle = len(guests_list) // 2

guests_list.insert(middle, "suiany")
print(guests_list)

guests_list.append("luiza")
print(guests_list)

print(f"\n{guests_list[0].title()}, it'll be a great pleasure for me to have you in this dinner;")
print(f"{guests_list[1].title()}, it'll be a great pleasure for me to have you in this dinner;")
print(f"{guests_list[2].title()}, it'll be a great pleasure for me to have you in this dinner;")
print(f"{guests_list[3].title()}, it'll be a great pleasure for me to have you in this dinner;")
print(f"{guests_list[4].title()}, it'll be a great pleasure for me to have you in this dinner;")
print(f"{guests_list[5].title()}, it'll be a great pleasure for me to have you in this dinner.")