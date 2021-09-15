# Program to find factorial of entered number.

import os
os.system("cls")

num = int(input("Enter the number to find factorial: "))
factorial=1

if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
    for i in range(1,num + 1):    
        factorial = factorial*i    

    print("The factorial of",num,"is",factorial)