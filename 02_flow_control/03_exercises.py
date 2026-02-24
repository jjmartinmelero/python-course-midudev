# Ejercicios
# Ejercicio 1: El mensaje secreto

# Dada la siguiente lista:

# Lista

mensaje = ["C", "o", "d", "i", "g", "o",
           " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje “secreto”.
print(mensaje[7:])

# Ejercicio 2: Intercambio de posiciones

# Dada la siguiente lista:

# Lista

numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

aux = numeros[0]
numeros[0] = numeros[4]
numeros[4] = aux

# alternative
# numeros[0], numeros[-1] = numeros[-1], numeros[0]

print(numeros)

# Ejercicio 3: El sándwich de listas

# Dada las siguientes listas:

# Listas

pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

sandwich = pan + ingredientes + pan_abajo

print(sandwich)


# Ejercicio 4: Duplicando la lista

# Dada una lista:

# Lista

lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados. Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]


duplicated_list = lista + lista
print(duplicated_list)


# Ejercicio 5: Extrayendo el centro

# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing. Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30.
lista = [10, 20, 30, 40, 50]
centro = len(lista) // 2
print(lista[centro])

# Ejercicio 6: Reversa parcial

# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación). Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6].

lista = [1, 2, 3, 4, 5, 6]

center = len(lista)//2

# another solution
lista_invertida = lista[:center][::-1] + lista[center:]

print(lista_invertida)
