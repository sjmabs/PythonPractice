# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

x = int(input("Give a number: "))
if x % 4 == 0:
    print("Even and Divisible by 4")
elif x % 2 == 0:
    print("Even")
else:
    print("Odd")

y = int(input("What shall we divide it by?: "))

if x%y == 0:
    print(f"{x} divided by {y} is {x/y}!")
else:
    print(f"{x} doesn't divide well by {y}. It would give you {y} lots of {int(x/y)} with {x%y} left over")


