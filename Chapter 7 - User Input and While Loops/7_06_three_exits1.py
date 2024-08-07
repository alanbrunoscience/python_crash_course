# Use a conditional test in the while statement to stop the loop.
prompt = "Enter a pizza's topping, please."
prompt += "\nEnter 'quit' to end the program: "

requested_topping = ""

while requested_topping != "quit":
    
    requested_topping = input(prompt)
    
    if requested_topping != "quit":
        print(f"\n-> Adding {requested_topping.lower()}.\n")

print("\nFinished making your pizza!")