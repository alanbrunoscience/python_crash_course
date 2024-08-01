cities = {
    "new york city": {
        "country": "usa",
        "population": 8_258_035,
        "fact": "More than 800 languages are spoken throughout the city",
    },
    
    "paris": {
        "country": "france",
        "population": 11_276_701,
        "fact": "The Louvre is the world’s most visited museum",
    },
    
    "london": {
        "country": "united kingdom",
        "population": 9_748_000,
        "fact": "The British government has employed cats since the 16th "
        "century",
    },
}

print("*** INFORMATION ABOUT CITIES ***\n")
for city, city_info in cities.items():
    print(f"-> City name: {city.title()};")
    if city_info['country'].lower() == "usa":
        print(f"-> Country: {city_info['country'].upper()};")
    else:
        print(f"-> Country: {city_info['country'].title()};")
    print(f"-> Population: {city_info['population']};")
    print(f"-> Fact: {city_info['fact']}.\n")