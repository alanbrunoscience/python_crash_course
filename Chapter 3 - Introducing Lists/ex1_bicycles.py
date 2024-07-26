bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

print(bicycles[1].title())
print(bicycles[3].title())

print(bicycles[-1].title()) # The last element in the list
print(bicycles[-2].title()) # The second element from the end of the list
print(bicycles[-3].title()) # The third element from the end of the list
print(bicycles[-4].title()) # The fourth element from the end of the list

message = f"My first bicycle was a {bicycles[0].title()}."

print(message)