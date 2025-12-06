'''
Day18: Regular Expression
Today's work:
1. Using regular expression in some samples
2. Using regular expression for searching
'''

'''
Note Part
The module of regular expression should be import
A quick way to search or match

re.match search in the begin of the first line
re.search search in the whole lines
re.findall return the list of matches
re.split split the string at the match point return a list
re.sub replace the matches within a string

well, it just like 'find' in Matlab; search is better than match if the txt has many lines; findall is best when the match
items are more than 1
however, how can we find the index?

'''

'''
Question Part

'''

# Main function
import re
txt = 'I love to learn python and javaScript'
match = re.match('I love to learn', txt, re.I)
print(match)
span = match.span()
print(span)
start, end = span
print(start)
print(end)
substring = txt[start:end]
print(substring)

match2 = re.match('matlab', txt, re.I)
print(match2)
find = re.findall('a', txt)
print(find)
# the re.I mean contains both lowercase and uppercase letters
match_replace = re.sub('javaScript', 'Matlab', txt)
print(match_replace)
