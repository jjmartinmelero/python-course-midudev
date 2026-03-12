
person = {
    "name": "Juan Jesus",
    "age": 32,
    "is_student": True,
    "califications": [7, 8, 9],
    "socials": {
        "twitter": "@jjmartinmelero",
        "instagram": "@jjmartinmelero",
        "facebook": "@jjmartinmelero"
    }
}


# access to the values:
print(person["name"])
print(person["socials"]["twitter"])


# update a var:
person["name"] = "a new name"
print(person)


# delete a property
del person["age"]
print(person)

is_student = person.pop("is_student")
print(is_student)
print(person)


# override a dictionary with other dictionary
a = {"name": "Name 1", "age": 20}
b = {"name": "Name 2", "is_student": True}

a.update(b)
print(a)

# check if exist an property
print("name" in person)
print("nombre" in person)


# get all keys
print(person.keys())

# get all values
print(person.values())

# get keys and values
print(person.items())


# iterate a dictionary:
for key, value in person.items():
    print(f"key: {key} -> value: {value}")
