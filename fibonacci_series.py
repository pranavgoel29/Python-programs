# Program to find Fibonnaci series.

import os
os.system("cls")

num= int(input("Enter the number of terms: "))
num1=0 
num2=1
count = 0
if num <= 0:
   print("Enter a positive integer")
elif num == 1:
   print("Fibonacci sequence upto",num,":")
   print(num1)
else:
   print("Fibonacci sequence:")
   while count < num:
       print(num1)
       nth = num1 + num2
       num1 = num2
       num2 = nth
       count += 1
