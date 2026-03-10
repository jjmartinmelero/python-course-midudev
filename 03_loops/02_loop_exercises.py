# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\n Exercise 1: ")
result = [num for num in range(1,21) if num % 2 == 0]
print(result)


# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números: numeros = [10, 20, 30, 40, 50] Calcula la media de los números usando un bucle for.
nums = [10, 20, 30, 40, 50]

total = 0

for num in nums:
    total += num    

print(f"average: {total / len(nums)}")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números: numeros = [15, 5, 25, 10, 20] Encuentra el número máximo en la lista usando un bucle for.
nums = [15, 5, 25, 10, 20]
biggest = 0

for number in nums:
    if number > biggest:
        biggest = number

print(biggest)


# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras: palabras = ["casa", "arbol", "sol", "elefante", "luna"] Crea una nueva lista que contenga solo las palabras con más de 5 letras usando un bucle for y list comprehension.

words = ["casa", "arbol", "sol", "elefante", "luna"]

new_words = [word for word in words if len(word) > 5]

print(new_words)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras: palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"] Pide al usuario que introduzca una letra. Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).

words = ["casa", "arbol", "sol", "elefante", "luna", "coche"]

user_letter = input("please, write a character:")

words_start_with_character = [word for word in words if word[0].lower() == user_letter.lower()]

print(f"total letters: {len(words_start_with_character)}")
