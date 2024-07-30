favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
        
# You can also use the keys() method to find out if a particular person 
# was polled. The keys() method isn’t just for looping: it actually 
# returns a sequence of all the keys.
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll.")