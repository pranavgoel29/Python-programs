# Program to take number as input till -1 is encountered and also count the negative, positive and zeroes entered by user.
import os
os.system("cls")

i = 0
a = 0
b = 0
c = 0

while(i<1):
    number = float(input("Enter a number: "))
    if number > 0:
        print("It is positive number")
        a = a + 1
    elif number == 0:
        print("It is Zero")
        b = b + 1
    else:
        print("It is a negative number")
        c = c + 1
        if(number==-1):
            break

print("Total no.of positive number: ", a)
print("Total no.of negative number: ", c)
print("Total no.of zero number: ", b)