guests_list = ['eusebio', 'jesus', 'suiany', 'jean', 'crisely', 'luiza']

print(guests_list)

print(f"\nGuys, I'm really sorry, but the new dinner table won't arrive" 
      " in time. So, I can invite only two people for dinner.\n")

list_length = len(guests_list)

while(list_length > 2):
    contact_removed = guests_list.pop()
    print(f"Sorry, {contact_removed.title()}! But I won't be able to "
          "welcome you to this dinner since the table didn't arrived on time.")
    list_length = len(guests_list)

print(f"\nRemaining guests: {guests_list}")

print(f"\n{guests_list[0].title()} and {guests_list[1].title()}, "
      "don't worry, but you are still invited to the dinner. :)")

print(f"\nRemoving the remaining guests from the guests list...")

del guests_list[0]
del guests_list[0]

print(f"\nRemaining guests: {guests_list}")