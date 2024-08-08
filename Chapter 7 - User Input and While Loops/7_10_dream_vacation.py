places = []

prompt = "-> If you could visit one place in the world, where would you go? "
prompt += "(Enter '0' to finish the program): "

polling_active = 1

print("--- POLL RESPONSES ---\n")

while polling_active:
    
    place = input(prompt)
    
    if place == '0':
        polling_active = False
    else:
        places.append(place.title())
        print()


# Count the repetitions for each place.
count_places = {}

for place in places:
    if place in count_places:
        count_places[place] += 1
    else:
        count_places[place] = 1
        

# Sorting the dictionary by keys.
sorted_places_count = dict(sorted(count_places.items()))

# Calculate the percentage of each place mentioned.
sum_count = sum(sorted_places_count.values())
   
print("\n\n--- POLL RESULT ---\n")
for place, count in sorted_places_count.items():
    print(f"-> {place}: {((count * 100) / sum_count):.2f}% ({count} people)")
    
print(f"\n-> Total number of people who participated in the poll: {sum_count}")
