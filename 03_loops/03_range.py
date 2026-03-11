

print("\n range")

nums = range(5)

for num in nums:
    print(num)


# range with step
for num in range(0, 10, 2):
    print(num)

# with negative numbers
for num in range(-5, 0):
    print(num)

for num in range(10, 0, -1):
    print(num)

# create a list from a range

range(10)
list_from_range = list(range(10))
print(list_from_range)