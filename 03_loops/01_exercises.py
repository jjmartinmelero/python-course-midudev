###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

counter = 10

while counter > 0:
    print(counter)
    counter -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

counter = 1
total = 0

while counter <= 20:
    if counter % 2 == 0:
        total += counter
    counter += 1
else:
    print(f"total: {total}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")


num_factorial = 5
total = 1

while num_factorial > 0:
    total *= num_factorial
    num_factorial -= 1
else:
    print(f"The factorial is: {total}")


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

invalid_password: bool = True

while invalid_password:
    user_password = input("Write your password: ")

    if len(user_password) >= 8:
        invalid_password = False
else:
    print('The password is valid')


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

user_number = int(input("Write a number: "))
counter = 1

while counter <= 10:
    print(f"{user_number} * {counter}: ", (user_number * counter))
    counter += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
# Un número es primo si es divisible por sólo uno de los números enteros entre 1 y él mismo, incluido.

print("\nEjercicio 6:")

n = int(input("Introduce un número entero positivo N: "))

numero = 2
while numero <= n:
    es_primo = True
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            es_primo = False
            break
        divisor += 1
    if es_primo:
        print(numero)

    numero += 1
