"""
Program to check if someone can vote. (18 and over and enrolled to vote)
1. Write with nested if's
2. Write with 'and' operator
"""

user_age = int(input("Enter age: "))
enrolled_to_vote = input("Are you enrolled to vote? Y/N ").upper()

# if user_age >= 18:
#     if enrolled_to_vote == 'Y':
#         print("ALLOWED to vote")
# else:
#     print("NOT ALLOWED to vote")

if user_age >=18 and enrolled_to_vote == 'Y':
    print("ALLOWED to vote")
else:
    print("NOT ALLOWED to vote")