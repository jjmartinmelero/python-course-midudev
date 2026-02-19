
# assign a var
my_name = "juan jesus"

print(my_name)

age = 22

print(age)

age = 32

print(age)


# Python variable typing is dynamic.
name = "test name"
print(type(name))

name = 33
print(type(name))


print(f"Hello {my_name}, I have {age} years old")


# not recomended
name, age, city = "juan jesus", 32, "Malaga"

# naming convention
my_var_name = "snake case"
name = "simple var name"

# pascal case is not used in python
# MyVarName = "Pascal"


# to create constants use UPPER_CASE
MY_CONSTANT = 3.14

# not valid vars name
#
# 234234_var = "ko"
# my-var = "ko"
# my var = "ko"


# add type to vars
is_user_logged_in: bool = True
print(is_user_logged_in)

# but you can override the type (and it's work in python)
is_user_logged_in = 34
print(is_user_logged_in)
