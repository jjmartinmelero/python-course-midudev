
# types conversion

# int
print("type conversion")

print(type("100"))

print(type(int("100")))

# error:
# print(2 + "100")

# str
print(str(2) + "100")

print(2 + int("100"))


# float
print(type(float("3.1416")))

print(int(3.1416))

# boolean
print(bool(3))

# Only 0 will be False
print(bool(0))

print(bool(-1))

print(bool(""))

print(bool(" "))

print(bool("False"))


# round a number
print(round(2.5))

print(round(3.5))
