places = ['nyc', 'bastogne', 'auschwitz', 'kehlsteinhaus', 'new zealand']

print(f"Original list: {places}")

print(f"Sorted list: {sorted(places)}")

print(f"Original list again: {places}")

print(f"Reverse sorted list: {sorted(places, reverse=True)}")

print(f"Original list again: {places}")

places.reverse()

print(f"Reversed list: {places}")

places.reverse()

print(f"Reverse list again (original order): {places}")

places.sort()

print(f"Permanent sorted list: {places}")

places.sort(reverse=True)

print(f"Permanent sorted list (reverse-alphabetical order): {places}")