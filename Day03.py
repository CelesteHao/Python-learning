'''
Day03: Operators
Today's work:
1. Use different operators
2. declare variables
3. Comparison Operators
4. Logical Operators

'''

'''
Note Part
>> means right shift n(in binary)
equals to /2**n
<< means left shift n(in binary)
equals to *2**n
% means modulus
// means floor division
| and & mean bitwise or and and?

Comparison Operators: 6 in total. ==; !=; >; <; >=; <=
And 4 comparison operator: is; is not; in; not in

Logical Operators: and; or; not
return ture: both ture; one is ture; False
'''

'''
Question Part
1.| and & mean bitwise or and and?
2.Comparison Operators return bool ?
3.How to use input to input coordinate like (3,4)?
'''

# Main Program
# Complex numbers
# print('Complex number: ', 1 + 1j)
# print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
#
# print('True == True: ', True == True)
# print('True == False: ', True == False)
# print('False == False:', False == False)
#
# print('1 is 1', 1 is 1)                   # True - because the data values are the same
# print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
# print('coding' in 'coding for all') # True - because coding for all has the word coding
# print('a in an:', 'a' in 'an')      # True
# print('4 is 2 ** 2:', 4 is 2 ** 2)   # True
#
# print(not not True)  # True
# print(not not False) # False



# Exercise
# 1.Write a script that prompts the user to enter base and height of
# the triangle and calculate an area of this triangle (area = 0.5 x b x h).

# base = float(input('base = '))
# height = float(input('height = ')) # input just can get an input value
# area_triangle = base * height / 2
# print(area_triangle)

# 2.Write a script that prompts the user to enter side a, side b, and side c of the triangle.
# Calculate the perimeter of the triangle (perimeter = a + b + c).

# a = float(input('side a = '))
# b = float(input('side b = '))
# c = float(input('side c = '))
# perimeter = a+b+c
# print(perimeter)

# 3.Calculate the slope, x-intercept and y-intercept of y = 2x -2

# slope=2
# x_intercept=1
# y_intercept=-2

# 4.Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

# slope = (10-2)/(6-2)
# euclidean_distance = ((10-2)**2+(6-2)**2)**0.5

# 5.Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

# y_being_0=False
# while y_being_0==False:
#   x=float(input('x= '))
#   y=x**2 + x*6 + 9
#   if abs(y)<0.1:
#       y_being_0=True
#       print('when x= ',x,'y= ',y,'y is going to be 0')
#   else:
#       y_being_0=False
#       print('y= ',y)


# 6.Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

# print(7//3 == 2.7)

# 7.Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

# x_1=1
# x_2=2
# x_3=3
# x_4=4
# x_5=5
# print(x_1,' ',x_1**0,' ',x_1**1,' ',x_1**2,' ',x_1**3)
# print(x_2,' ',x_2**0,' ',x_2**1,' ',x_2**2,' ',x_2**3)
# print(x_3,' ',x_3**0,' ',x_3**1,' ',x_3**2,' ',x_3**3)
# print(x_4,' ',x_4**0,' ',x_4**1,' ',x_4**2,' ',x_4**3)
# print(x_5,' ',x_5**0,' ',x_5**1,' ',x_5**2,' ',x_5**3)

# for x in range(1,6):# python not consider the last number(like 6 in this line)
#     print(x,' ',x**0,' ',x**1,' ',x**2,' ',x**3)





