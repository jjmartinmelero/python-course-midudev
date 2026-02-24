

# listas
list1 = [1, 2, 3, 4, 5]
list2 = ["test1", "test2", "test3", "test4"]
list3 = [1, "hello", True, 3.4]
empty_list = []
list_of_lists = [[1, 2], [3, 4]]
matrix = [[1, 2], [2, 3], [3, 4]]

print(list1)
print(list2)
print(list3)
print(empty_list)
print(list_of_lists)
print(matrix)


# get elements
print("\n get elements by index")
print(list2[0])
print(list2[-1])  # test4
print(list2[-2])  # test3

# access element with matrix
print(list_of_lists[1][0])


# slicing
list1 = [1, 2, 3, 4, 5]

print(list1[1:4])

# 3 first
print(list1[:3])

# 3 last
print(list1[3:])


# copy of list
print(list1[:])


# copy list with a new iteration
print(list1[::2])


# reverse list
print(list1[::-1])


# update a element in a list
list1[0] = 20
print(list1)

# in python we can't update a position that does not exist
# list1[20] = 200 --> ERROR


# less efficient
list1 = list1 + [10, 20, 30]
print(list1)

# more efficient
list1 += [40, 50, 60]

print(list1)

# get length of list
print("length of list: ", len(list1))
