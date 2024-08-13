# You can go a step further by storing your functions in a separate file 
# called a module and then importing that module into your main program. 
# An import statement tells Python to make the code in a module available 
# in the currently running program file;

# To call a function from an imported module, enter the name of the 
# module you imported, pizza, followed by the name of the function, 
# make_pizza(), separated by a dot;

# The best approach is to import the function or functions you want, 
# or import the entire module and use the dot notation.

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

