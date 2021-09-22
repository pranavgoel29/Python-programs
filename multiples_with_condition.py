# Program which iterates integer from 1 to 50. For multiple of three print `Fizz` instead of the number and for the multiple of the five print `Buzz`. And for the number which is multiple of both three and five print `FizzBuzz`

import os
os.system("cls")

for i in range(1,50):
    if(i%3 == 0):
        print("\nThe multiple of 3:\nFizz")
    if(i%5 == 0):
        print("\nThe multiple of 5:\nBuzz")
    if(i%3 == 0 and i%5 == 0):
        print("\nThe multiple of both 3 and 5:\nFizzBuzz")