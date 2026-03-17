
import re

# point (.) -> any chart

text = 'Hello world !, H$llo again !'
pattern = 'H.llo'

found = re.findall(pattern, text)

print(found)

#  example 2
text = 'Hola mundo, Hola de nuevo. Casa, cosa, cisa, ceca, causa.'
pattern = r'c.sa'
results = re.findall(pattern, text)
print(results)


# search the a point (.) -> scape a character
text = 'Mi casa es blanca. El coche es negro.'
pattern = r'\.'
results = re.findall(pattern, text)
print(results)


# search a digit -> \d (found any digit 0-9)

text = 'the phone number is 68812356789'
digits = re.findall(r'\d{9}', text)

print(digits)


# search a spain phone number +34 .....

text = 'My phone number is -> +34 688999999'
pattern = r'\+34 \d{9}'
found = re.search(pattern, text)

print(found.group())


# \w -> any alphanumeric character (a-z, A-Z, 0-9, _)
text = 'my_nick_name_90'
pattern = r'\w'
found = re.findall(pattern, text)
print(found)


# \s -> any blank space (space, tab, line break)
text = 'hello world\n how are you ? '
pattern = r'\s'
found = re.findall(pattern, text)
print(found)


# ^ -> coincides with the beginning of the string
user_name = "%423_name"
pattern = r"^\w"  # validate user name

is_valid = re.search(pattern, user_name)

if is_valid:
    print("User is valid !")
else:
    print("user is not valid")


# validate a phone number
phone = "+34 666666666"
pattern = r"\+\d{2,3}"

valid = re.search(pattern, phone)

if valid:
    print("Phone number is valid !")
else:
    print("phone number is not valid")


# $ -> coincides with the end of the chain
text = "Hello world"
pattern = "world$"

valid = re.search(pattern, text)

if valid:
    print("string is valid !")
else:
    print("string is not valid")


# \b -> coincides with the beginning or end of a word
text = "casa casada cosa cosas casado"
pattern = r"\bc.sa\b"
found = re.findall(pattern, text)
print(found)


# | -> match with one option or the other
fruits = "plátano, manzana, aguacate, pera"
pattern = r'aguacate|palta|p..a'
matches = re.findall(pattern, fruits)
print(matches)
