# Use an active variable to control how long the loop runs.
prompt = "Enter a pizza's topping, please."
prompt += "\nEnter 'quit' to end the program: "

active = True
while active:
    requested_topping = input(prompt)
    
    if requested_topping == "quit":
        active = False
    else:
        print(f"\n-> Adding {requested_topping.lower()}.\n")

print("\nFinished making your pizza!")