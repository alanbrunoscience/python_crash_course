sandwich_orders = []
finished_sandwiches = []

active_orders = True

print("--- SANDWICH ORDERS ---\n")

while active_orders:

    sandwich_name = input("- Enter the name of the sandwich, please: ")
    
    sandwich_orders.append(sandwich_name.title())
    
    repeat = input("\n-> Would you like to continue to make new" 
                   " orders (yes/no)? ").strip().lower()
    
    while (repeat != "yes") and (repeat != "no"):
        repeat = input("\n-> Invalid option. Choose 'yes'"
                       " or 'no': ").strip().lower()
    
    if repeat == "no":
        active_orders = False
    else:
        print()


print("\n\n--- WARNING ---\n")
print("-> The pastrami is gone! Removing pastrami sandwich orders, if has...")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
    

print("\n\n--- ORDERS STATUS ---\n")
while sandwich_orders:
    
    current_sandwich = sandwich_orders.pop(0)
    
    if sandwich_orders and current_sandwich != sandwich_orders[-1]:
        print(f"-> {current_sandwich.title()} sandwich is made;")
    else:
        print(f"-> {current_sandwich.title()} sandwich is made.")
    
    finished_sandwiches.append(current_sandwich)
  
      
print("\n\n--- SANDWICHES ORDERED ---\n")
for sandwich in finished_sandwiches:
    if sandwich != finished_sandwiches[-1]:
        print(f"-> {sandwich.title()} sandwich;")
    else:
        print(f"-> {sandwich.title()} sandwich.")