# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
# Extras:
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous
# message. (Hint: order of operations exists in Python)
#
# Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n is the same as pressing the ENTER button)

import datetime

now = datetime.datetime.now()

name = input("Enter your name: ")
age = int(input("Enter your age: "))
had = input("Have you had your birthday this year yet?(y/n): ")
msg = f"Hello {name}, You are currently {age}. You will turn 100 in the year {now.year + 100 - age}. "
if had.lower() == "y":
    print(msg)
else:
    msg = f"Hello {name}, You are currently {age}. You will turn 100 in the year {now.year + 99 - age}. "
    print(msg)


num = int(input("give me a number: "))
print(msg*num)
print("or we can print it like this")
msg += "\n"
print(msg * num)
