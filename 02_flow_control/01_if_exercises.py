# Ejercicios prácticos
# Ejercicio 1: Determinar el mayor de dos números

# Pide al usuario que introduzca dos números y muestra un mensaje indicando cuál es mayor o si son iguales.

user_number_1 = input("write a number: ")
user_number_2 = input("write a second number: ")

if user_number_1 > user_number_2:
    print(f"{user_number_1} > {user_number_2}")
elif user_number_1 < user_number_2:
    print(f"{user_number_1} < {user_number_2}")
else:
    print(f"{user_number_1} == {user_number_2}")


# Ejercicio 2: Calculadora simple

# Pide al usuario dos números y una operación (+, -, *, /). Realiza la operación y muestra el resultado (maneja la división entre cero).


try:

    user_number_1 = int(input("write a number: "))
    user_number_2 = int(input("write a second number: "))
    operation = input("choose your operation (+, -, *, /): ")

    if operation == '/' and user_number_2:
        print(user_number_1 / user_number_2)

    if operation == '+':
        print(user_number_1 + user_number_2)

    if operation == '-':
        print(user_number_1 - user_number_2)

    if operation == '*':
        print(user_number_1 * user_number_2)

except ValueError:
    print(ValueError)

# Ejercicio 3: Año bisiesto

# Pide al usuario que introduzca un año y determina si es bisiesto:

# Es divisible por 4.
# Excepto si es divisible por 100, pero no por 400.


anio = int(input("Introduce un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")

# Ejercicio 4: Categorizar edades

# Clasifica una edad ingresada por el usuario en:

# Bebé (0-2 años)
# Niño (3-12 años)
# Adolescente (13-17 años)
# Adulto (18-64 años)
# Adulto mayor (65 años o más)


age = int(input("how old are you ? : "))

if 0 <= age <= 2:
    print("Bebé")
elif 3 <= age <= 12:
    print("Niño")
elif 13 <= age <= 17:
    print("Adolescente")
elif 18 <= age <= 64:
    print("Adulto")
elif age >= 65:
    print("Adulto mayor")
else:
    print("Edad no válida.")
