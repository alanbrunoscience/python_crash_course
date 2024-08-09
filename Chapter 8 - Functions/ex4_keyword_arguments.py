# A keyword argument is a name-value pair that you pass to a function. 
# Keyword arguments free you from having to worry about correctly ordering 
# your arguments in the function call, and they clarify the role of each 
# value in the function call.
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")
    
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')