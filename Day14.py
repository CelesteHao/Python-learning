'''
Day14:Higher Order Functions
Today's work:
1. Handling functions as parameters
2. Returning functions as return value from another functions
3. Using Python closures and decorators

'''


'''
Notes: 


'''

'''
Question Part

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
        return num + ten
    return add
# what is this line mean?
closure_result = add_ten()
# not useful
# add_ten(5)
print(closure_result(5))  # 15
print(closure_result(10))  # 20

# sample 3: Decorators
# it is confused
# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
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
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

