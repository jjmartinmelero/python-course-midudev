

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


character_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# delete a range of elements
del character_list[2:5]

print(character_list)
