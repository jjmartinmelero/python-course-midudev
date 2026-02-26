

list = [1, 2, 3, 4, 5]

list.append(6)

print(list)


character_list = ['a', 'b', 'c', 'd']
character_list.append('e')

print(character_list)

# insert a element in a position
character_list.insert(1, '@')
print(character_list)


# add several elements in the end of the list
character_list.extend(['test', 'test2'])

print(character_list)


# remove a element
# (the first element in the list)
character_list.remove("@")
print(character_list)

# return and delete the last element in the list
last_element = character_list.pop()
print(last_element)
print(character_list)

# delete second element in the list
character_list.pop(1)
print(character_list)


# alternative
del character_list[-1]
print(character_list)


# delete all list element
character_list.clear()
print(character_list)


numbers = [10, 5, 3, 4, 5, 3, 2, 8, 9]
# delete a range of elements
del numbers[2:5]

print(numbers)


# order list
numbers.sort()
print(numbers)

# create a new list
numbers = [10, 5, 3, 4, 5, 3, 2, 8, 9]
sorted_numbers = sorted(numbers)
print(numbers, sorted_numbers, sep='\n')


# order string list -- all minus
fruits = ['apple', 'banana', 'lemon', 'cherry']
sorted_fruits = sorted(fruits)
print(sorted_fruits)

# with some mayus and minus
fruits = ['apple', 'Banana', 'lemon', 'Cherry']
sorted_fruits = sorted(fruits)
print(sorted_fruits)
fruits.sort(key=str.lower)
print(fruits)


# more utils methods
animals = ['animal1', 'animal2', 'animal3', 'animal4', 'animal5']
print(len(animals))
print(animals.count('animal2'))

# check an element:
print('animal8' in animals)
print('animal2' in animals)
