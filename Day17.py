'''
Day15: Exception Handling
Today's work:
1. use try and except to skip the error, avoiding breaking out
2. Packing and Unpacking Arguments in Python
3. Enumerate and Zip in Python
'''

'''
Note Part
Python uses try and except to handle errors gracefully.
unlike matlab, python can exit error, in case of some error in a large function.

lst 
*lst : * can unpack the list

use the packing method to allow our function to take unlimited number or arbitrary number of arguments
'''

'''
Question Part
what time should use unpacking?
Answer:
if the function need numbers of input, but just had a list or tuple;
if need to print all the value instead of list

why this part can have 2 parameter?
# for index, item in enumerate([20, 30, 40]):
#     print(index, item)
enumerate can unpack of a list
print(list(enumerate([20, 30, 40])))
[(0, 20), (1, 30), (2, 40)]
and the parameter in for loop can be tuple unpacking


'''

# Main Program
# try:
#     print(10 + '5')
# except:
#     print('Something went wrong')

# try:
#     name = 'hao'
#     year_born = 's'
#     age = 2019 - year_born
#     print(f'You are {name}. And your age is {age}.')
# except TypeError as e:
#     print('Type error occured')
#     print('Type error:', e)
# except ValueError:
#     print('Value error occured')
# except ZeroDivisionError:
#     print('zero division error occured')

# def sum_of_five_nums(a, b, c, d, e):
#     return a + b + c + d + e
#
# lst = [1, 2, 3, 4, 5]
# # print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
# print(sum_of_five_nums(*lst))
#
# numbers = range(2, 7)  # normal call with separate arguments
# print(list(numbers)) # [2, 3, 4, 5, 6]
# args = [2, 7]
# numbers = range(*args)  # call with arguments unpacked from a list
# print(numbers) # range(2, 7)
# # as day14 test, print(numbers) just output range(2, 7), not [2, 3, 4, 5, 6]
# print(list(numbers))

# countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# fin, sw, nor, *rest = countries
# print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
# numbers = [1, 2, 3, 4, 5, 6, 7]
# one, *middle, last = numbers
# print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7

# packing
# use * as input of function
# def sum_all(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
# print(sum_all(1, 2, 3))             # 6
# print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
#
# for index, item in enumerate([20, 30, 40]):
#     print(index, item)
#
# print(list(enumerate([20, 30, 40])))
#
# data = [(1,2,3), (4,5,6)]
# for a, b, c in data:
#     print(a, b, c)

# fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
# if len(fruits) != len(vegetables)
# the zip will stop when get the last index, even if the other list is not end
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion']
fruits_and_veges = []
# for f, v in zip(fruits, vegetables):
#     fruits_and_veges.append({'fruit':f, 'veg':v})
# print(fruits_and_veges)

from itertools import zip_longest
# the fillvalue='Missing' is also useful
for f, v in zip_longest(fruits, vegetables, fillvalue=None):
    print(f, v)
