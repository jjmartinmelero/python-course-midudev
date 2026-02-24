

print("\n Basic booleans: ")

print(True)
print(False)

print("\n Comparation operators: ")
print("5 > 3:", 5 > 3)
print("5 < 3:", 5 < 3)
print("5 == 3:", 5 == 3)
print("5 != 3:", 5 != 3)
print("5 >= 3:", 5 >= 3)
print("5 <= 3:", 5 <= 3)


print("\n Comparation strings")
print("manzana" < "pera")  # True
print("Hola" == "hola")  # False


print("\n Logic operators: ")

print(True and True)   # True
print(True and False)  # False
print(True or False)   # True
print(False or False)  # False
print(not True)        # False
print(not False)       # True


print("\n Tabla de la verdad:")
print("and:")

print("A        B       A and B")
print("True     True    ", True and True)
print("True     False   ", True and False)
print("False    True    ", False and True)
print("False    False   ", False and False)


print("or:")

print("A        B       A or B")
print("True     True    ", True or True)
print("True     False   ", True or False)
print("False    True    ", False or True)
print("False    False   ", False or False)

print("not:")

print("A not A")
print("True ", not True)
print("False ", not False)
