import re

# [ -> matches with any character inside the brackets

user_name = "ju.an_123"
pattern = r"[\w._%+-]+"

if re.fullmatch(pattern, user_name):
    print("Valid username")
else:
    print("Invalid username")

#search all vowels in a text
text = "Hello world"
pattern = r"[aeiouAEIOU]"
matches = re.findall(pattern, text)
print(matches)

#exercise 2
text = 'man fan van ran nyan'

result = re.findall(r'[mfb]an', text)
print(result)  # Salida: ['man', 'fan', 'van']