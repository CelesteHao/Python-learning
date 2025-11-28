'''
Day14:Higher Order Functions
Today's work:
1. Handling functions as parameters
2. Returning functions as return value from another functions
3. Using Python closures and decorators
4. map/reduce/filter built-in function

'''

'''
Notes: 
It's very interesting that map() can't do the calculate when be called
for example ,when print(map()), the output is '<map object at 0x0000020F5BC823B0>'
when print(list(map())), the output is '[1, 4, 9, 16, 25] '
so it use no memory

'''


'''
Question Part
For filter, is there any way to keep false and drop true?
Yes,
1. in the judgement statement, use not
2. use not in the filter
3. filterfalse (which should be import: 'from itertools import filterfalse')



'''

# Main Program
# sample 1
# def sum_numbers(nums):  # normal function
#     return sum(nums)    # a sad function abusing the built-in sum function :<
#
# def higher_order_function(f, lst):  # function as a parameter
#     summation = f(lst)
#     return summation
# result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
# print(result)       # 15

# sample 2: Python Closures
# why the part: return add is not return add(), the function should has() for no factor parameter
def add_ten():
    ten = 10
    def add(num):
        # add can access the external variable
        return num + ten
    return add
# what is this line mean?
closure_result = add_ten()
# not useful
# closure_report = add_ten
# closure_report = add_ten and 5 right?
# add_ten(5)
print(closure_result(5))  # 15
print(closure_result(10))  # 20

# sample 3: Decorators
# get a function, return a new function, execute the new function
# Normal function
def greeting():
    return 'Welcome to Python'
# (function) means accept a function as input not number/list
def uppercase_decorator(function):
    # a new closure, wrapper can access 'function'
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
# this 'greeting' is the function
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator
'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
# this line equals to g = uppercase_decorator(greeting)
# the decorator'@' should close to a function
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

# map function
# map can take a function and iterable as parameters
# replacement of for loop
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(numbers_squared) # the output is <map object at 0x0000020F5BC823B0>
print(list(numbers_squared))
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Let's apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

# filter function
# Lets filter only even numbers
numbers = [1, 2, 3, 4, 5]  # iterable
def is_even(num):
    if num % 2 == 0:
        return True
    return False
even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

# reduce function
# can be replaced by for, the logic is confused
from functools import reduce
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)
total = reduce(add_two_nums, numbers_str)
print(total)    # 15

# Exercise

# Explain the difference between map, filter, and reduce.
'''
The three function can accept a function and a iterable object as input.
map function will return a iterator, and if use list() or other can output the result;
filter will drop false and keep true;
reduce should be import in Python3, and will return as the function's return, however reduce() has a initializer as the third input,
which calculate from the initializer.

'''

# Use map to change each name to uppercase in the names list
names_list = ['hao zhang','yanling zhou']
def uppercase_list(name):
    return name.upper()
names_uppercase = map(uppercase_list, names_list)
print(names_uppercase)
print(list(names_uppercase))
# if I just want the first character uppercase?
names_uppercase_first = map(lambda name: name.title(), names_list)
print(list(names_uppercase_first))