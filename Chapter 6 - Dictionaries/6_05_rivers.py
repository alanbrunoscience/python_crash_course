rivers = {
    'nile': 'egypt',
    'amazon river': 'brazil',
    'mississippi river': 'united states',
}

print("*** RIVERS AND THEIR COUNTRIES ***\n")
for river, country in rivers.items():
    print(f"-> The {river.title()} runs through {country.title()}.")
    
print("\n\n*** RIVERS' NAME ***\n")
for river in rivers.keys():
    print(f"-> {river.title()}.")
    
print("\n\n*** COUNTRIES' NAME ***\n")
for country in rivers.values():
    print(f"-> {country.title()}.")

