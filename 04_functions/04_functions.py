

def greeting():
    print("Hello !!")


greeting()


def greeting_to(name):
    print(f"Hello, {name}")


greeting_to("Juan Jesus")


def add(a, b):
    return a + b


print(f"add function: {add(10, 5)}")

# document function with docstring:


def subtract(a, b):
    """Subtract two numbers and return the result"""
    subtract = a - b
    return subtract


# access to the documentation:
print(subtract.__doc__)


# param by default:
def multiply(a, b=2):
    return a * b


print(multiply(2))
print(multiply(2, 3))


def describe_person(name, age):
    print(f"I'm {name} and i am {age} years old !")


# arguments by position:
describe_person("Juan Jesus", 32)

# arguments by key:
describe_person(age=32, name="juan jesus")


# length of arguments
def add_numbers(*args):
    sum = 0
    for num in args:
        sum += num

    return sum


print(
    f"add numbers with a unknow number of parameters: {add_numbers(1, 2, 3, 4, 5)}")


# arguments with key and value variable: (**args)

def show_information_of(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_information_of(name="Juan Jesus", age=32, direction="Alameda, Malaga")
show_information_of(last_name="Martin Melero", age=2,
                    direction="Alameda, Malaga")
