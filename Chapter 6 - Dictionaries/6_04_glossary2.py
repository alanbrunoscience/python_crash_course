programming_words = {
    'Variable': 'A storage location identified by a memory address and a symbolic name (an identifier), which contains some known or unknown quantity of information referred to as a value',
    'Array': 'A collection of elements identified by index or key, where each element is the same data type',
    'Class': 'A blueprint for creating objects (a particular data structure), defining a set of attributes and methods that the objects created from the class can have',
    'Data Structure': 'A way of organizing and storing data in a computer so that it can be accessed and modified efficiently. Examples include arrays, linked lists, stacks, queues, and trees',
    'Function': 'A block of organized, reusable code that performs a single action. Functions usually take inputs, process them, and return an output',
}

print("*** GLOSSARY ***\n")
for word, meaning in programming_words.items():
    print(f"{word}:\n\n -> {meaning}.\n")