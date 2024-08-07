# Use a break statement to exit the loop when the user enters a 'quit' value.
prompt = "Enter a pizza's topping, please."
prompt += "\nEnter 'quit' to end the program: "

while True:
    requested_topping = input(prompt)
    
    if requested_topping == "quit":
        break
    else:
        print(f"\n-> Adding {requested_topping.lower()}.\n")

print("\nFinished making your pizza!")