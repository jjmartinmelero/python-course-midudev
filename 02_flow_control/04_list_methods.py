

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
