def describe_city(city_name, country="USA"):
    print(f"-> {city_name.title()} is in {country.title()}.")
    

describe_city('new york')
describe_city(city_name='san diego')
describe_city(city_name='são paulo', country='brazil')
describe_city('london', 'england')