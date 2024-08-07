hobbies = ['soccer', 'karate', 'read', 'play guitar', 'watch movies']

print(f"*** ORIGINAL LIST ***\n\n{hobbies}")

print("\n-----------------------------------------------------------\n")

print("*** ACCESSING ELEMENTS IN A LIST ***\n")

print(f"-> 1º Element: {hobbies[0].title()};")
print(f"-> 2º Element: {hobbies[1].title()};")
print(f"-> 3º Element: {hobbies[2].title()};")
print(f"-> 4º Element: {hobbies[3].title()};")
print(f"-> 5º Element: {hobbies[4].title()}.")

print("\n-----------------------------------------------------------\n")

print("*** MODIFYING ELEMENTS IN A LIST ***\n")

hobbies[0] = 'volleyball'
hobbies[1] = 'run'

print(f"-> Modified list: {hobbies}")

print("\n-----------------------------------------------------------\n")
      
print("*** APPENDING ELEMENTS TO THE END OF THE LIST ***\n")

hobbies.append('karate')

print(f"-> New list: {hobbies}")

print("\n-----------------------------------------------------------\n")
      
print("*** INSERTING ELEMENTS INTO THE LIST ***\n")

hobbies.insert(0, 'travel')

print(f"-> New list: {hobbies}")

print("\n-----------------------------------------------------------\n")

print("*** REMOVING AN ITEM USING THE del STATEMENT ***\n")

del hobbies[-1]

print(f"-> New list: {hobbies}")

print("\n-----------------------------------------------------------\n")

print("*** REMOVING AN ITEM USING THE pop() METHOD ***\n")

popped_hobby = hobbies.pop()

print(f"-> Removed element: '{popped_hobby}';\n")
print(f"-> New list: {hobbies}")

print("\n-----------------------------------------------------------\n")

print("*** POPPING ITEMS FROM ANY POSITION IN THE LIST ***\n")

popped_hobby = hobbies.pop(0)

print(f"-> Removed element: '{popped_hobby}';\n")
print(f"-> New list: {hobbies}")

print("\n-----------------------------------------------------------\n")

print("*** REMOVING AN ITEM BY VALUE ***\n")

removed_element = 'volleyball'

hobbies.remove(removed_element)

print(f"-> Removed element: '{removed_element}';\n")
print(f"-> New list: {hobbies}")

print("\n-----------------------------------------------------------\n")

print("*** SORTING THE LIST PERMANENTLY WITH THE sort() METHOD ***\n")

hobbies.sort()

print(f"-> Sorted list: {hobbies}")

print("\n-----------------------------------------------------------\n")

print("*** SORTING THE LIST IN REVERSE ALPHABETICAL ORDER ***\n")

hobbies.sort(reverse=True)

print(f"-> Sorted list in reverse alphabetical order: {hobbies}")

print("\n-----------------------------------------------------------\n")

print("*** SORTING THE LIST TEMPORARILY WITH THE sorted() FUNCTION ***\n")

print(f"-> Current list: {hobbies};\n")

print(f"-> Sorted list temporarily: {sorted(hobbies)}")

print("\n-----------------------------------------------------------\n")

print("*** PRINTING THE LIST IN REVERSE ORDER ***\n")

print(f"-> Current list: {hobbies};\n")

hobbies.reverse()

print(f"-> Reversed list: {hobbies}")

print("\n-----------------------------------------------------------\n")

print("*** FINDING THE LENGTH OF THE LIST ***\n")

print(f"-> Current list: {hobbies};\n")

print(f"-> The length of the current list is: {len(hobbies)}.\n")