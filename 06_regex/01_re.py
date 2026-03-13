

# regular expressions

# first step -> import the module re
import re

#create a pattern (it is a string that contains the rules to find the text)
pattern = r"Hello"

# text to search
text = "Hello, my name is Juan Jesus and I am 32 years old."

# use re.search(pattern, text) to find the pattern in the text
result = re.search(pattern, text)


if result:
    print("Pattern found")
else:
    print("Pattern not found")
