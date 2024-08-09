def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")
    
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')