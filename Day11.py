'''
Day10:Functions(important part)
Today's work:
1. Create functions
2. use return to get result from function

'''


'''
Notes: 
If we do not know the number of arguments we pass to our function, 
we can create a function which can take arbitrary number of arguments by adding * before the parameter name.

when use function(*value)
the *value always be tuple!

'''

'''
Question Part
1. should the Arbitrary Number of Parameters must in the end of Default Parameters?
yes must!
'''

# Main Program
# def function_one():
#     lst1 = [1, 2, 3]
#     return lst1
#
# def function_two(rangeup):
#     if type(rangeup) is int:
#         pass
#     else:
#         print('rangeup is not int')
#         return
#     lst1 = list(range(1,rangeup,1))
#     return lst1
#
# def function_three(rangeup = 10):
#     if type(rangeup) is int:
#         pass
#     else:
#         print('rangeup is not int')
#         return
#     lst1 = list(range(1,rangeup,1))
#     return lst1
#
# print(function_two(10))
# print(function_three())

# def function_three(*rangeup):
#     if type(rangeup) is int:
#         pass
#     elif type(rangeup) is tuple:
#         rangeup = rangeup[0]
#         pass
#     else:
#         print('rangeup is not int or list of ints')
#         return
#     lst1 = list(range(1,rangeup,1))
#     return lst1
# print(function_three(10,11))


# Exercise
# Write a function called is_prime, which checks if a number is prime.
# Write a functions which checks if all items are unique in the list.
# Write a function which checks if all the items of the list are of the same data type.
# Write a function which check if provided variable is a valid python variable


# def is_prime(number):
#     if number < 2:
#         print('Please enter a number >= 2')
#         return False
#     elif number == 2:
#         return True
#     else:
#         for div_num in range(2,number,1):
#             if number % div_num == 0:
#                 return False
#     return True
# number = int(input('Enter an int number: '))
# print(is_prime(number))

# def is_unique(lst): # transfer lst to set, and compare if length is same
#     len_lst = len(lst)
#     len_set = len(set(lst))
#     if len_set == len_lst:
#         return True
#     else:
#         return False
#
# lst = list(input('Enter a list: (use comma to separate ').split(sep = ','))
# print(is_unique(lst))

# def is_unique(lst): # transfer lst to set, and compare if length is same
#     type_item = type(lst[0])
#     for item in lst[1:]:
#         if type_item == type(item):
#             return False
#
# lst = list(input('Enter a list: (use comma to separate) ').split(sep = ','))
# print(is_unique(lst))

# valid name requirement
# 1. just contain _ number charaters
# 2. begin without number
# def check_valid(lst):
#     if type(lst[0]) is int:
#         return False
#     for item in lst:
#         if type(item) is int:
#            pass
#         elif item.isalpha() is True:
#            pass
#         elif item == '_':
#            pass
#         else:
#             return False
#
#     return True
#
# while True:
#     lst = input('Enter a variable name: ')
#     if lst == 'exit':
#         break
#     print(check_valid(list(lst)))