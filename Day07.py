'''
Day06:Set
Today's work:
1. create a set
2. basic method of set(base on maths)


'''


'''
Notes: 
Set is a collection of unordered and un-indexed distinct elements. and unique!
difference means st1(first) - st2(second)


nowadays, I have learnt 3 different types of elements.
list:[]
tuple:(): no change
set:{}: unique


'''

'''
Question Part

'''

# Main Program
# st = set()
# st = {'item1', 'item2', 'item3','item4'}
#
# # union or update
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item5', 'item6', 'item7', 'item8'}
# st3 = st1.union(st2)
# st1.update(st2)
#
# # Intersection
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item3', 'item2'}
# st_intersection = st1.intersection(st2)
#
# # Ubset and Super Set and difference
# st2.issubset(st1) # True , mean st1 contains st2
# st1.issuperset(st2) # True , mean st2 is in st1 (the same above)
# st2.difference(st1) # set()
# st1.difference(st2) # {'item1', 'item4'} => st1\st2
#
# # Finding Symmetric Difference Between Two Sets
# # it means (A\B)∪(B\A)
# # syntax
# st2.symmetric_difference(st1) # {'item1', 'item4'}
#
# # check joint
# st2.isdisjoint(st1) # False

# Exercise
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# 2. Explain the difference between the following data types: string, list, tuple and set
# 3. I am a teacher and I love to inspire and teach people.
#    How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
len_list = len(age)
len_set = len(age_set)
print('length of age list is {}, length of age set is {}'.format(len_list, len_set))

# String: contain characters/words and every character have index(blank is also a character)
# List: contain items and every item have index
# Tuple: the same as list but can't be changed
# Set: the same as list but every item is unique and have not index

sentence_str = 'I am a teacher and I love to inspire and teach people.'
list_str = sentence_str.split(sep=' ')
print(list_str) # check result of split
uniquewords = len(set(list_str)) # tran to set and counts
print('unique words in list is {}'.format(uniquewords))



