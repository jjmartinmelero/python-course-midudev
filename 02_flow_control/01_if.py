
import os

os.system("clear")

print("simple conditional statement")


age = 18

# if
if age >= 18:
    print("you are of legal age")


print("conditional statement with else")

age = 15
# if and else

if age >= 18:
    print("you are of legal age")
else:
    print("you are not legal age :(")


print("conditional statement with elif")

exam_grade = 7

if exam_grade >= 9:
    print("Excellent !")
elif exam_grade >= 7:
    print("Good performance")
elif exam_grade >= 5:
    print("in the limit")
else:
    print("fail")


print("Multiple conditions:")
age = 25
has_license = True

if age >= 18 and has_license:
    print("you can drive")
else:
    print("Warning ! you can't drive")


# in another city....
if age >= 18 or has_license:
    print("you can drive in this city !")
else:
    print("you can't drive here....")


is_weekend = False

# use 'not'
if not is_weekend:
    print("is not weekend")
else:
    print("yuhu ! is weekend !")


print("nest conditions: ")
age = 20
has_money = True

if age >= 18:
    if has_money:
        print("you can go to the cinema")
    else:
        print("Stay home")
else:
    print("You can't go to the cinema")


if < 18:
    print("You can't go to the disco")
elif has_money:
    print("you can go to the disco")
else:
    print("stay home")
