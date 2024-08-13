def city_country(city_name, country):
    return f'"{city_name.title()}, {country.title()}"'

print("--- Data Input ---\n")
for i in range(3):
    print(f"{i+1}º:\n")
    city_name = input(f"-> Enter a city name: ")
    country = input(f"-> Enter the country of the city informed: ")
    
    print(f"\n{city_country(city_name, country)}")
    
    print('\n----------------------------\n')

# Or:

# print(city_country('santiago', 'chile'))
# print(city_country('rio de janeiro', 'brazil'))
# print(city_country('hong kong', 'china'))