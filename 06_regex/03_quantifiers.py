
import re

# * -> puede aparecer 0 o mas veces

text = "aaaba"
pattern = r"a*"
matches = re.findall(pattern, text)
print(matches)


# + -> una o mas veces
text = "dddddaaaacccc"
pattern = "a+"

matches = re.findall(pattern, text)
print(matches)


# ? -> zero or once
text = "aaabacb"
pattern = "a?b"
matches = re.findall(pattern, text)
print(matches)


# exercise
phone = '+34 666666666'

# Patrón: El prefijo +34 es opcional
pattern = r'\+34? \d{9}'

# Búsqueda de coincidencias
if re.search(pattern, phone):
    print('Número de teléfono válido encontrado.')
else:
    print('Número de teléfono no válido.')
