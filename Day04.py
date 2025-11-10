'''
Day04: Strings
Today's work:
1. declare and link strings
2. format a set of variables enclosed in string
3. Unpacking Characters
4. Slicing and Reversing a String
5. String Methods


'''

'''
Note Part
just use '+' can link strings
\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")

The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), 
together with a format string, which contains normal text together with "argument specifiers", 
special symbols like "%s", "%d", "%f", "%.number of digitsf".
for example, formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
just like print('I am ' + first_name + ' ' + last_name)
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision

in python 3
str.format can also use the method by using {}
formated_string='I am {} {}'.format(first_name,last_name)
f.string used in python3.6+

a='python'[0] true
a='python'(0) false
to start from right, a='python'[-1]

Reversing a String
'python'[::-1]

A lot of String Methods
string_declared = 'python'
capitalize(): Converts the first character of the string to capital letter
count(): returns occurrences of substring in string, count(substring, start=.., end=..).
endswith(): Checks if a string ends with a specified ending
ect.

hash = '#'

'''

'''
Question Part
No question

'''

# Main Program
string_formatted = 'I\'m learning Python!'
print('the string length: ',len(string_formatted))
print('P appear first time at: ' ,string_formatted.find('P'))
print('n appear last time at: ',string_formatted.rfind('n'))

# The following list contains the names of some of python libraries:
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
list_formatted = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
string_formatted = '#'.join(list_formatted)
print(string_formatted)

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
str1 = 'I am enjoying this challenge.'
str2 = 'I just wonder what is next.'
print(str1 + '\n' + str2)

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = float(input('radius = '))
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius, area))
