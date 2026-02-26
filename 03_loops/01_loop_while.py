
# while loop
print("Loop while: ")
counter = 0

while counter < 5:
    print(counter)
    counter += 1


# use break inside loop (exit)
print("Loop while with break: ")
counter = 0

while True:
    print(counter)
    if counter > 5:
        break
    counter += 1

# use continue inside loop (skip an iteration)
print("Loop while with continue: ")
counter = 0

while counter < 10:
    counter += 1

    if counter % 2 == 0:
        continue

    print(counter)


# loop while with else (not work when we use break to exit loop)
print("Loop while with else: ")

counter = 0

while counter < 5:
    print(counter)
    counter += 1
else:
    print("loop finished")


# get a user number
number = -1

while number < 0:
    try:
        number = int(input("Write a positive number: "))
        if number < 0:
            print("the number should be positive... try again :(")
    except:
        print("You should write a number...")


print(f"The usernumber is: {number}")
