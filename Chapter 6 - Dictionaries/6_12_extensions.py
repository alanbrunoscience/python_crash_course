movies = {
    "Mrs. Doubtfire": {
        "Directed by": "Chris Columbus",
        "Category": "Dramatic Comedy",
        "Cast": ['Robin Williams', 'Sally Field', 'Pierce Brosnan', 'Harvey '
                 'Fierstein', 'Robert Prosky'],
        "Distributed by": "20th Century Fox",
    },
    
    "The Devil Wears Prada": {
        "Directed by": "David Frankel",
        "Category": "Comedy-drama",
        "Cast": ['Meryl Streep', 'Emily Blunt', 'Anne Hathaway', 'Stanley '
                 'Tucci', 'Simon Baker', 'Adrian Grenier'],
        "Distributed by": "20th Century Fox",
    },
    
    "The Lord of the Rings": {
        "Directed by": "Peter Jackson",
        "Category": "Epic fantasy adventure",
        "Cast": ['Elijah Wood', 'Ian McKellen', 'Liv Tyler', 'Viggo '
                 'Mortensen', 'Sean Astin', 'Cate Blanchett', 'John '
                 'Rhys-Davies', 'Christopher Lee', 'Billy Boyd', 'Dominic '
                 'Monaghan', 'Orlando Bloom', 'Hugo Weaving', 'Andy Serkis',
                 'Sean Bean'],
        "Distributed by": "New Line Cinema",
    },
}

print("*** MY FAVORITE MOVIES ***\n")
for movie_name, movie_info in movies.items():
    print(f"-> Movie name: {movie_name}")
    for key, value in movie_info.items():
        if key.lower() == "cast":
            print(f"-> {key.title()}:", end=" ")
            for name in value:
                if name != value[-1]:
                    print(f"{name.title()},", end=" ")
                else:
                    print(f"{name.title()}")
        else:
            print(f"-> {key.title()}: {value.title()}")
    print()