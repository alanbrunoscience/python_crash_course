def count_duplicates(names, prices, weights):
    from collections import defaultdict
    
    # Create a dictionary to count occurrences of each (name, price, weight) tuple
    product_count = defaultdict(int)
    
    # Populate the dictionary with counts
    for name, price, weight in zip(names, prices, weights):
        product_key = (name, price, weight)
        product_count[product_key] += 1
    
    # Calculate the number of duplicates
    duplicates = 0
    for count in product_count.values():
        if count > 1:
            duplicates += (count - 1)  # (count - 1) gives the number of duplicates
    
    return duplicates

# Example Usage
names = ['ball', 'box', 'ball', 'ball', 'box']
prices = [2, 2, 2, 2, 2]
weights = [1, 2, 1, 1, 3]

print(count_duplicates(names, prices, weights))  # Output: 2
