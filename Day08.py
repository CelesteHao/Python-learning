'''
Day08:Dictionary
Today's work:
1. Creat dictionary
2. get item from dictionary
3. Add item and key to dictionary
4. Remove item

'''


'''
Notes: 
A dictionary is a collection of unordered, modifiable(mutable) *paired* (key: value) data type. 
access Dictionary items by referring to its key name.

'''

'''
Question Part

'''

# Main Program
dct = { # declare a dictionary for exercise
    'name': 'EddyProcess',
    'user': 'Hao',
    'creat_time': '11/11',
    'modify_time': ['11/11', '11/12'],
    'SND': 'True',
    'WPL': 'True',
    'input_format': 'netcdf',
    'output_format': 'dat'
}
print(len(dct))
print('input files format: {}'.format(dct['input_format']))
print('input files format: {}'.format(dct.get('input_format'))) # avoid no key in dict

dct['Frequency correction'] = 'False' # add item and key
dct['modify_time'].append('11/13')
print(dct)

dct.pop('SND')
print('use pop: ',dct)
dct.popitem()
print('use popitem: ',dct)
del dct['WPL']
print('use del: ' ,dct)
print(dct.items()) # transfer and split the dictionary to list
keys = dct.keys() # get keys
values = dct.values() # get values

# Exercise

