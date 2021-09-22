#program to perform arithematic operations or known as simple calculator.

import os
os.system("cls")

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
  
  
# Take input from the user 
select = int(input("Select operations form 1, 2, 3, 4 :"))
  
val_1 = int(input("Enter first number: "))
val_2 = int(input("Enter second number: "))

if select == 1:
    print(val_1, "+", val_2, "=",val_1+val_2)

if select == 2:
    print(val_1, "-", val_2, "=",val_1-val_2)

if select == 3:
    print(val_1, "*", val_2, "=",val_1*val_2)

if select == 4:
    print(val_1, "/", val_2, "=",val_1/val_2)