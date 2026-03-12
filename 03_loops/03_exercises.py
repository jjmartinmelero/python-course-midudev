# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\n exercise 1")
for num in range(1, 11):
    print(num)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\n exercise 2")
for num in range(20):
    if (num + 1) % 2 != 0:
        print(num + 1)


# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\n exercise 3")
for num in range(4, 20):
    if (num + 1) % 5 == 0:
        print(num + 1)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\n exercise 4")
for num in range(10, 0, -1):
    print(num)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\n exercise 5")
total = 0

for num in range(100):
    total += (num + 1)

print(f"total: {total}")


# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime su tabla de multiplicar del 1 al 10 usando un bucle for y range().

user_number = int(input("please, write a number: "))

for idx, num in enumerate(range(10)):
    print(f"{user_number} x {idx + 1} = {user_number * (idx + 1)}")
