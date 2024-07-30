# Looping Through All Values in a Dictionary

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print("The following languages have been mentioned:\n")
for language in favorite_languages.values():
    print(language.title())
    
# To see each language chosen without repetition, we can use a set. 
# A set is a collection in which each item must be unique.
print("\n\nThe following languages have been mentioned (without repetition):\n")
for language in set(favorite_languages.values()):
    print(language.title())