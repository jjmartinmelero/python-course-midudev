# En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es clave para enfrentar desafíos. En este ejercicio, nos centraremos en dos miembros de la alianza:

# Reed Richards (Mr. Fantastic), representado por la letra R.
# Johnny Storm (La Antorcha Humana), representado por la letra J.
# El objetivo es crear una función en Python que reciba una cadena de texto y cuente cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la letra J (para Johnny Storm). La función debe tener los siguientes comportamientos:

# Si la cantidad de R y la cantidad de J son iguales, la alianza está en equilibrio y la función debe retornar True.
# Si las cantidades no son iguales, la función debe retornar False.
# Si no aparece ninguna de las dos letras en la cadena, se considera que el equilibrio se mantiene, por lo que la función debe retornar True.



def check_is_balanced(text):
    text = text.upper()

    # count the number of times a letter appears
    count_r = text.count("R") # Reed Richards
    count_j = text.count("J") # Johnny Storm
    
    print(f"count_r: {count_r} count_j: {count_j}")

    return count_r == count_j


print(check_is_balanced("RRJJ"))
print(check_is_balanced("RRRRJJ"))
print(check_is_balanced("RRJJJJJJ"))
print(check_is_balanced("awwwaqAQAQA"))