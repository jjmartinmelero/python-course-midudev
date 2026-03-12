# En Jurassic Park, los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. En este ejercicio, se nos proporciona una lista de números enteros que representan la cantidad de huevos puestos por diferentes dinosaurios en el parque.

# Objetivo
# Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros, es decir, la suma de todos los números pares en la lista.

def count_carnivore_dinosaur_eggs(egg_list) -> int:
    """
    This function takes a list of integers representing the number of eggs laid by different 
    dinosaurs in Jurassic Park, with even numbers indicating carnivores. 
    It returns a number representing the sum of all carnivore eggs.
    """

    total_carnivore_eggs = 0

    for eggs in egg_list:
        if eggs % 2 == 0:
            total_carnivore_eggs += eggs

    return total_carnivore_eggs


print(count_carnivore_dinosaur_eggs([3, 4, 7, 5, 8]))
