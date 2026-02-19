

# get user information
print("Hello, what is your name ?")
name = input()

print(f"Hello {name} ! nice to meet you :)")

age = input("how old are you ?\n")

print(f"In the nex 20 years, you will have {int(age) + 20}")


print("Get several values: ")
country, city = input("Which is your country and city ? ").split()

print(country, city)
