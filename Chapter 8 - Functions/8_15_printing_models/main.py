import printing_models as pd

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pd.print_models(unprinted_designs, completed_models)
pd.show_completed_models(completed_models)