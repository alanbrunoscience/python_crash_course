# To make the middle name optional, we can give the middle_name argument 
# an empty default value and ignore the argument unless the user provides 
# a value.
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    