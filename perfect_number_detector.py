# Program to find the inputted number is perfect or not.

import os
os.system("cls")

n = int(input())
sum = 0
for x in range(1, n):
    if n % x == 0:
        sum += x
if(sum == n):
    print("The entered number is Perfect.")
else:
    print("The entered number is not Perfect.")
