

# regular expressions

# first step -> import the module re
import re

# create a pattern (it is a string that contains the rules to find the text)
pattern = r"Hello"

# text to search
text = "Hello, my name is Juan Jesus and I am 32 years old."

# use re.search(pattern, text) to find the pattern in the text
result = re.search(pattern, text)


if result:
    print("Pattern found")
else:
    print("Pattern not found")


# get the match pattern
print(result.group())

# get initial position of math pattern
print(result.start())

# get last position of math pattern
print(result.end())


# exercise 1
text = 'This is an evaluation text about AI and its impact.'
patron = 'AI'

matches = re.search(patron, text)

if matches:
    print(
        f'Pattern found in the position {matches.start()}-{matches.end()}')
else:
    print('Pattern not found.')


# exercise 2 - Get all coincidences
# findAll
text = 'I like Python. Python is amazing. Learning Python is fun.'
pattern = 'Python'
matches = re.findall(pattern, text)

print(matches)


# exercise 3 - iterate match result
text = 'I like Python. Python is amazing. Learning Python is fun.'
pattern = 'Python'
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())


# ignorecase in the search
text = 'I like PytHon. python is amazing. Learning pytHOn is fun.'
pattern = 'Python'
matches = re.findall(pattern, text, re.IGNORECASE)

print(matches)


# replace the text (replace all coincidences)

text = 'Hello world !, Hello again !'
pattern = 'Hello'
replacement = 'Goodbye'
new_text = re.sub(pattern, replacement, text)

print(new_text)
