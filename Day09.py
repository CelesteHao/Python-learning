'''
Day09:Condition
Today's work:
1. Know condition structure
2. Conditional execution and Repetitive execution

'''


'''
Notes: 
elif = else if
It's like the other languages' condition, but because of no 'end' in python, the text-indent must be set strictly.
True in bool can be written as 'True'

'''

'''
Question Part

'''

# Main Program

# a = int(input("Enter a number: "))
# b = input("Enter another number: ")
# if a > 0:
#     print('A is a positive number')
# elif a < 0:
#     print('A is a negative number')
# else:
#     print('A is zero')

# Exercise
# Here we have a person dictionary.
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') -
# for more accurate results more conditions can be nested!
# If the person is married and if he lives in Finland, print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.
if 'skills' in person:
    len_skills = len(person['skills'])
    if len_skills % 2 ==1:
        print('the middle skill is ', person['skills'][len_skills//2])
    else:
        print('the middle skill is ', person['skills'][len_skills//2 - 1], ' and ', person['skills'][len_skills//2])

if 'skills' in person:
    if 'Python' in person['skills']:
        print('Python is in skills')
    else:
        print('Python is not in skills')

if 'JavaScript' in person['skills'] and 'React' in person['skills'] and len(person['skills']) == 2:
    print('JavaScript is in skills')
if 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a backend developer')


if person['country'] == 'Finland' and person['is_marred'] == True:
    print('Asabeneh Yetayeh lives in Finland. He is married.')
