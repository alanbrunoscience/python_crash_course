def make_shirt(size, message):
    print(f"-> T-Shirt Size: {size};")
    print(f"-> T-Shirt Message: '{message.title()}'")


def validate_size(size):
    while size < 34 or size > 46:
        size = int(input("\n-> Invalid size! The value needs to be equal "
                     "to or greater than 34 and less than or equal to 46: "))
    return size


print("--- MAKING T-SHIRTS ---\n")
size = input("1) Enter t-shirt size: ")
size = int(size)

size = validate_size(size)

if size < 38:
    message = input("\n2) Enter the message to be plotted on the t-shirt: ")
elif size <= 46:
    message = "I love Python."

print("\n\n--- T-SHIRT INFO ---\n")
make_shirt(size, message)