# You can define a default value for each parameter. If an argument for 
# a parameter is provided in the function call, Python uses the argument 
# value. If not, it uses the parameter’s default value.

def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# Note: When you use default values, any parameter with a default 
# value needs to be listed after all the parameters that don’t have 
# default values. This allows Python to continue interpreting positional
# arguments correctly.