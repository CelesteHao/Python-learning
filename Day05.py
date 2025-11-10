'''
Day05: Lists
Today's work:
1. Creat list
2. Unpacking list
3. Add and insert items into list
4. Remove item in list

'''

'''
Notes: 
List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

A list index starts from 0.  use negative number start from right
[0,1,2,3] [-4,-3,-2,-1]

first_item, second_item, third_item, *rest = lst
the * is important, but no need to set in the end
first_item, second_item, *rest, third_item = lst

insert will shift the origin item to right
so can't insert item to the end, use append

Remove item
remove(): target item
pop(): specific index
del : more flexible and remember: del list[1:2] just delete list[1]!

Clear
lst.clear(): []
del lst: None lst

Copy
lst2 = lst.copy()

Extend
lst.extend(lst2) means extend lst2 to the end of lst

Count
lst.count(1) means count 1 in lst

Index
lst.index(1) will return where is 1

Reverse
lst.reverse() will reverse lst

Sort
lst.sort()
lst.sort(reverse=True)

'''

'''
Question Part

'''

# Main Program
lst = list()
# lst = [] # the same
lst.append('time')
lst.insert(0, 'location')
lst.insert(-1,'figure')
print(lst)

lst.sort() # ascend
lst.sort(reverse=True) # descend
lst.sort(reverse=False) # ascend
print(sorted(lst))


# Exercise
# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
# Add the min age and the max age again to the list
# Find the median age (one middle item or two middle items divided by two)
# Find the average age (sum of all items divided by their number )
# Find the range of the ages (max minus min)
# Compare the value of (min - average) and (max - average), use abs() method
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] # given list
ages.sort()
print('the sorted ages are',ages)
min_age = ages[0]
max_age = ages[-1]
ages.append(max_age) # add max_age right
ages.insert(0, max_age) # add min_age left
print('the append ages are',ages)
ages_len = len(ages)
median_index = 0 # define if ages_len == 1
if ages_len%2 == 1 :
    median_index = (ages_len-1)//2
if ages_len%2 == 0 :
    median_index = ages_len//2
print('the median age is {}'.format(ages[median_index]))

median_age = ages[median_index]
average_age = sum(ages)/len(ages)
range_age = max_age - min_age
min_ave_age = abs(min_age - average_age)
max_ave_age = abs(max_age - average_age)
if min_ave_age > max_ave_age :
    print('min-average {} is higher than max-average {}'.format(min_ave_age, max_ave_age))
else :
    print('max-average {} is lower than min-average {}'.format(max_ave_age, max_ave_age))






