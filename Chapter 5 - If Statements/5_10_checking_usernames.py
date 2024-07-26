current_users = ["admin", "alanbruno", "john_sena", "airton_senna", 
             "eusebio_nogueira"]

new_users = ["Admin", "Alanbruno", "John_sena", "kezia_rosa", 
             "juliana_souza"]

# Transforming the list to lowercase
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"-> You need to enter a new username! '{new_user}' "
              "is already in use.")
    else:
        print(f"-> The '{new_user}' is available.")