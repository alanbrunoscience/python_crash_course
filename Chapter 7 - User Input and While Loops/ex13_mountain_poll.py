responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

print("--- POLL RESPONSES ---\n")

while polling_active:
    
    # Prompt for the person's name and response.
    name = input("-> What is your name? ")
    response = input("-> Which mountain would you like to climb someday? ")
    
    # Store the response in the dictionary.
    responses[name] = response
    
    # Find out if anyone else is going to take the poll.
    repeat = input("\n-> Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    else:
        print()
        
# Polling is complete. Show the results.
print("\n\n--- POLL RESULTS ---\n")
for name, response in responses.items():
    print(f"-> {name.title()} would like to climb {response.title()}\n")