print("*** FALSE PREDICTIONS ***\n")

car_1 = 'subaru'
car_2 = 'bmw'

if car_1.lower() == car_2.lower():
    answer = True
else:
    answer = False

print(f"1) Is {car_1.title()} a {car_2.upper()}?")
print(f"-> The prediction is {answer}!")

#=======================================================================

car_1 = 'porsche'

if car_1.lower() == car_2.lower():
    answer = True
else:
    answer = False

print(f"\n2) Is {car_1.title()} a {car_2.upper()}?")
print(f"-> The prediction is {answer}!")

#=======================================================================

car_1 = 'audi'

if car_1.lower() == car_2.lower():
    answer = True
else:
    answer = False

print(f"\n3) Is {car_1.title()} a {car_2.upper()}?")
print(f"-> The prediction is {answer}!")

#=======================================================================

car_1 = 'ferrari'

if car_1.lower() == car_2.lower():
    answer = True
else:
    answer = False

print(f"\n4) Is {car_1.title()} a {car_2.upper()}?")
print(f"-> The prediction is {answer}!")

#=======================================================================

car_1 = 'lamborghini'

if car_1.lower() == car_2.lower():
    answer = True
else:
    answer = False

print(f"\n5) Is {car_1.title()} a {car_2.upper()}?")
print(f"-> The prediction is {answer}!")

#=======================================================================

print("\n\n*** TRUE PREDICTIONS ***\n")

n1 = 10
n2 = 15

if n1 < n2:
    print(f'1) {n1} is less than {n2}. The prediction is {True}!\n')
else:
    print(f'1) {n1} is greater than {n2}. The prediction is {False}!\n')
    
#=======================================================================
    
if n1 <= n2:
    print(f'2) {n1} is less than or equal to {n2}. The prediction is {True}!\n')
else:
    print(f'2) {n1} is greater than {n2}. The prediction is {False}!\n')
    
#=======================================================================

n1 = n2

if n1 == n2:
    print(f'3) {n1} is equal to {n2}. The prediction is {True}!\n')
else:
    print(f'3) {n1} is different from {n2}. The prediction is {False}!\n')
    
#=======================================================================

names = ['alan', 'aline', 'bruna', 'carlos', 'duda']

name = 'alan'

answer = (name in names)

if (name in names):
    print(f'4) {name.title()} is in the names list. The prediction is {answer}!')
else:
    print(f'4) {name.title()} is not on the names list. The prediction is {answer}!')

#=======================================================================

name = 'aline'

answer = (name in names)

if (name in names):
    print(f'\n5) {name.title()} is in the names list. The prediction is {answer}!')
else:
    print(f'\n5) {name.title()} is not on the names list. The prediction is {answer}!')

#=======================================================================

print("\n\n*** AND & OR ***\n")

num_01 = 21

if num_01 >= 10 and num_01 <= 20:
    print(f'1) {num_01} is between 10 and 20 (including).')
else:
    print(f'1) {num_01} is not between 10 and 20 (including).')

#=======================================================================

num_01 = 15

if num_01 <= 10 or num_01 > 20:
    print(f"\n2) Is '{num_01}' less than or equal to 10 or greater than 20? {True}.")
else:
    print(f"\n2) Is '{num_01}' less than or equal to 10 or greater than 20? {False}.")
    
#=======================================================================

print("\n\n*** 'IN' OR 'NOT IN' ***\n")

blocked_users = ['andrew', 'carolina', 'david']

user = 'alan'

if user not in blocked_users:
    print(f"-> {user.title()}, you are allowed to access the application.")
else:
    print(f"-> {user.title()}, you are not allowed to access the application.")