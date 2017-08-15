"""Marnie Auld"""

name = input("Enter your name: ")
while name == "":
    print("Invalid Input - Please try again")
    name = input("Enter your name: ")

print(name[::2])