usernames = ["admin", "alanbruno", "john_sena", "airton_senna", 
             "eusebio_nogueira"]

for username in usernames:
    if username == "admin":
        print(f"Hello '{username.lower()}', would you like to see a status report?")
    else:
        print(f"Hello '{username.lower()}', thank you for logging in again.")