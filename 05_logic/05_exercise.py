# Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud. Cada número en lista_a se enfrenta al número en la misma posición en lista_b. Dependiendo de cuál de los dos números sea mayor, se aplica una regla y se continúa con el siguiente número en la lista.
# Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
# Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
# Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.
# Al final del proceso, se debe devolver el resultado de la batalla. Si al final queda un número en lista_a, se debe devolver ese número seguido de la letra “a”. Si queda un número en lista_b, se debe devolver ese número seguido de la letra “b”. En caso de empate, se debe devolver la letra “x”.


# Función para simular la batalla entre dos listas
def battle(lista_a, lista_b):
    points_a = sum(lista_a)
    points_b = sum(lista_b)
    return f"{points_a - points_b}a" if points_a > points_b else f"{points_b - points_a}b" if points_b > points_a else "x"


# Example 1
list_a = [4, 4, 4]
list_b = [2, 8, 2]
winner = battle(list_a, list_b)
print(winner)  # Result: "x"

# Example 2
list_a = [2, 4, 2]
list_b = [3, 3, 4]
winner = battle(list_a, list_b)
print(winner)  # Result: "2b"
