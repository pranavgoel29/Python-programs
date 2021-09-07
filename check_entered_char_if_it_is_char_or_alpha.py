# Program to determine the character entered by the user.

import os
os.system("cls")

print("Enter any character:")
a = input()
if a.isalpha() :
    print("\n" + a
    , "is a Alphabet.")
elif a.isdigit() :
    print("\n" + a, "is a Digit.")
else :
    print("\n" + a, "is a Special char.")