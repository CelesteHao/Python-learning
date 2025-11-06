'''
Day01: Introduction
Today's work:
1. Have a brief view of python
2. Know how to open and exit python interactive shell
3. Error types
4. Math expression
5. Indentation
6. Data types

'''

'''
Note Part
python --version: 3.13.5
Python is an interpreted scripting language, so it does not need to be compiled.
' '," ",''' ''' are all okay for string with '' '' not, and ''' ''' can be used in different line(can use enter type
string more than 1 line until type the other part 3*' )

number: integer, float, complex
string
boolean(True/False)
list(just like array)
Dictionary{'xx':'xx'}
Tuple(can't be changed)
set(unique items){}



'''

'''
Question Part
1. Why it shows different in pycharm terminal and WSL? and in WSL, python --version command can't be used?
python3 version was defined as 'python3'
2. What is the difference between interpreted and compiled code/language?
3. SyntaxWarning: "is" with 'int' literal. What is it mean?
is check pointing/ == check value
4. Difference between """""" and '''''' ?
no difference, appear in twins
5. List(just like array?) and can contain different data types?
yes
6. How to print the result in terminal?
'sys package need to be import'

'''
# Main program
# Exercise
# the following 1 line don't work
# print(python --version)
# use package of sys
import sys
print(sys.version)
print(type(sys.version))
print({'name':'hao'})
print(type({'name':'Hao'}))

import numpy as np
import pandas as pd
list = [1,2,3]
print(type(list))
print(np.array(list)+1)

test=np.array(list)+1
print(type(test))

# Find an Euclidian distance between (2, 3) and (10, 8)
# use **0.5 as sqrt
distance = ((10-2)**2+(8-3)**2)**0.5
print(distance)