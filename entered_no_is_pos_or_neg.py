# Program to test whether a number entered by the user is negative or positive or equal to zero.

import os
os.system("cls")

number = float(input("Enter a number: "))
if number > 0:
   print("It is positive number")
elif number == 0:
   print("It is Zero")
else:
   print("It is a negative number")