# function which return reverse of a string

import os
os.system("cls")
 
def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = str(input("Enter the string:- \n"))
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")