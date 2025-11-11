'''
Day06:Tuples
Today's work:
1. Creat Tuple
2. join/check/del tuple
3. transfer tuple to list

'''


'''
Notes: 
A tuple is a collection of different data types which is ordered and unchangeable (immutable). 
Tuples are written with round brackets, ().
No add, insert, remove items
but can del whole tuple


'''

'''
Question Part

'''

# Main Program
empty_tuple = () # empty tuple
week_tuple = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
len(week_tuple)
last_index = len(week_tuple) - 1
last_item = week_tuple[last_index]
print(last_item)
weekday_tuple = week_tuple[0:5]
weekend_tuple = week_tuple[5:]
week_lst = list(weekday_tuple)
week_lst_tuple = tuple(week_lst)
check_in_tuple = 'Tuesday' in week_tuple
print(check_in_tuple)
week_tuple_joint = weekday_tuple + weekend_tuple
print(week_tuple_joint)
del week_tuple_joint


# Exercise