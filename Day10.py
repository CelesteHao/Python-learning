'''
Day10:Loops
Today's work:
1. While loops
2. For loops
3. The Range Function

'''


'''
Notes: 
Break: We use break when we like to get out of or stop the loop.
Continue: With the continue statement we can skip the current iteration, and continue with the next.
Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
all types above can be used.
range(start, end, step) takes three parameters: starting, ending and increment.
In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors.
Also we can use it as a placeholder, for future statements.
'''

'''
Question Part

'''

# Main Program
# lst1 = list(range(1, 11, 1))
# lst2 = list(range(11))
# print(lst1 == lst2) # False because python start from 0

# for number in range(11):
#     print(number)   # prints 0 to 10, not including 11
# else:
#     print('The loop stops at', number)
# # else can be used at the for loop end
# for number in range(11):
#     pass

# Exercise
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit_list = ['banana', 'orange', 'mango', 'lemon']
fruit_list_reverse = []
# for fruit in fruit_list:
#     fruit_list_reverse.insert(0, fruit_list[fruit_list.index(fruit)]) # fruit is string yet, not a good way
for fruit in fruit_list:
    fruit_list_reverse.insert(0, fruit)
print(fruit_list_reverse)




