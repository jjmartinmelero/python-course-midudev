

print("\n Loop for: ")

fruits = ["apple", "banana", "cherry", "orange",
          "strawberry", "watermelon", "pineapple", "pear"]

for fruit in fruits:
    print(fruit)


# iterate a string
string = "juan jesus"

for character in string:
    print(character)


# use enumerate
for index, fruit in enumerate(fruits):
    print(f"index: {index} fruit: {fruit}")


# nest loops
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

for letter in letters:
    for number in numbers:
        print(f"{letter} x {numbers} = {letter * number}")


# example with break
print("\n break:")
animals = ['dog', 'cat', 'bird']

for animal in animals:
    if animal == "cat":
        break

    print(animal)

# example with continue
print("\n continue:")
animals = ['dog', 'cat', 'bird']

for animal in animals:
    if animal == "cat":
        continue

    print(animal)

# list comprehension
animals_upper_case = [animal.upper() for animal in animals]

print(animals_upper_case)


# displays even numbers
result = [num for num in [1, 2, 3, 4, 5, 6, 7] if num % 2 == 0]
print(result)
