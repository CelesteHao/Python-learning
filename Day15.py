'''
Day15: Python Type Errors
Today's work:
1. the various types errors in Python(showed in the main program part)

'''

'''
Note Part
Today's work is to know and test every type of error, if meet in further, I can know the way to fix them;
These errors are very basic, however, the function is based on the basic part.
'''

'''
Question Part


'''

# Main Program
# SyntaxError :
# print 'hello world'
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

# NameError :
# print(age)
# NameError: name 'age' is not defined

# IndexError :
# numbers = [1, 2, 3, 4, 5]
# numbers[5]
# IndexError: list index out of range

# ModuleNotFoundError :
# import maths
# ModuleNotFoundError: No module named 'maths'

# AttributeError
# import math
# math.PI
# AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?

# KeyError
# users = {'name':'Asab', 'age':250, 'country':'Finland'}
# print(users['name'])
# print(users['county'])
# KeyError: 'county'

# TypeError
# a = 4 + '3'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ImportError
# from math import power
# ImportError: cannot import name 'power' from 'math' (unknown location)

# ValueError
# int('12a')
# ValueError: invalid literal for int() with base 10: '12a'

# ZeroDivisionError
# a = 1/0
# ZeroDivisionError: division by zero

