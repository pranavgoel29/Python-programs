# Program to print the triangle pattern.

import os
os.system("cls")

n = 5

# outer loop to handle number of rows
# n in this case
for i in range(0, n):
        
    # values changing acc. to outer loop
    for j in range(0, i+1):
            
        # printing stars
        print("* ",end="")
        
    # ending line after each row
    print("\r")