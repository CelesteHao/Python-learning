'''
Day13:List Comprehension
Today's work:
1. use list comprehension to create a list
2. lambda list

'''

'''
Notes: 
list comprehension:
lst = [x * 2 for x in range(5)]

create a lits
lst = []
for x in range(5):
    lst.append(x * 2)

so list comprehension can in a compact way of creating a list from a sequence.

Lambda function is a small anonymous function without a name. 
It can take any number of arguments, but can 'only have one expression'. 
We need it when we want to write an anonymous function inside another function.
no need to declare

'''

'''
Question Part

'''
# Main Program
language = 'Python'
lst = [i for i in language]
print(lst)

squares = [i * i for i in range(11)]
print(squares)
# the part equals to
# for i in range(11):
#     squares[i] = i*i

# Generating even numbers
# can add selected conditions
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

add = lambda x, y: x + y
print(add(1, 2))

def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5)
print(two_power_of_five)  # 32

# Exercise
# Filter only negative and zero in the list using list comprehension
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_zero_number = [i for i in numbers if i<=0]
print(negative_zero_number)

# Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32)]
target_tuple = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(3)]
print(target_tuple)

factorial = lambda x: (x, x**0, x**1, x**2, x**3, x**4, x**5)
target_tuple = [factorial(i) for i in range(3)]
print(target_tuple)

# Write a lambda function which can solve a slope or y-intercept of linear functions.
def f_given():
    x1=2
    x2=3
    y1=5
    y2=4
    return [x1,y1,x2,y2]

point_1_lst = list(input('Point 1: '))
point_1 = [int(i) for i in point_1_lst if i.isdigit()] # use .isdigit() to skip the character if not digit
point_2_lst = list(input('Point 2: '))
point_2 = [int(i) for i in point_2_lst if i.isdigit()]
solve_slope = lambda point_1, point_2 : (point_2[1] - point_1[1])/(point_2[0] - point_1[0])
print(solve_slope(point_1,point_2))