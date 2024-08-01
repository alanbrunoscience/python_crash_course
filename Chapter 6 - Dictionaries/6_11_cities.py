cities = {
    "new york city": {
        "country": "USA",
        "population": 8_258_035,
        "fact": "More than 800 languages are spoken throughout the city.",
    },
    
    "paris": {
        "country": "France",
        "population": 11_276_701,
        "fact": "The Louvre is the world’s most visited museum.",
    },
    
    "london": {
        "country": "United Kingdom",
        "population": 9_748_000,
        "fact": "The British government has employed cats since the 16th "
        "century.",
    },
}

print("*** INFORMATION ABOUT CITIES ***\n")
for city, info in cities.items():
    print(f"-> City name: {city.title()}")
    for key, value in info.items():
        print(f"-> {key.title()}: {value}")
    print()