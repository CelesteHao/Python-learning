'''
Day02: Variables, Builtin Functions
Today's work:
1. Built-in Function
2. Define variable
3. Transfer types of variable


'''

'''
Note Part
Built-in Function means no need to import
In paper(--More--) enter 'P' to exit
A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.
(and should give more description)
Variable name cannot start with a number; case-sensitive; no - % @ 
Use underscore character after each word for a variable containing more than one word



'''

'''
Question Part
1. What are keywords/reserved words? Do they means no defined by myself?
yes not to define myself
2. How to sum('a','b'). It says use ''.join(seq)?
use other function to transfer ascall


'''

# Main Program

# first_name = input('What is your name: ')
# age = input('How old are you? ')
#
# print(first_name)
# print(age)

# Exercise
first_name='Hao'
last_name='Zhang'
full_name='Hao Zhang'
country='China'
city='Zhenjiang'
is_married='False' # string
is_married_bool=False # bool
year, month, day = 1999, 5, 23

name_length = len(full_name)
print(max([last_name, first_name], key=len))

# Define num_one and num_two
num_one=5.3
num_two=2.4
# Find floor division of num_one by num_two and assign the value to a variable floor_division
total=num_one+num_two
total_floor_division=int(total)
total_floor_division_round=round(total)

# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.
# radius=30 #unit m
radius = input('radius = ')
radius = float(radius) # the input function just
area_of_circle=radius**2*3.14 # no bulit-in function can define pi
print('area_of_circle:', area_of_circle)
circum_of_circle=radius*2*3.14
print('circle_area:', circum_of_circle)


