print('*** Using the range() Function ***\n')

for value in range(1, 6):
    print(value) # print value from 1 to 5 (including)

print('\n')

for value in range(6): 
    print(value) # print value from 0 to 5 (including)
    
print('\n*** Using range() to Make a List of Numbers ***\n')

numbers = list(range(1, 6))
print(numbers)