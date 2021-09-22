# Program which iterates integer from 1 to 50. For multiple of three print `Fizz` instead of the number and for the multiple of the five print `Buzz`. And for the number which is multiple of both three and five print `FizzBuzz`

import os
os.system("cls")

for i in range(1,51):
    
    if(i%3 == 0):
        print("The multiple of 3:\nFizz")
        continue
    if(i%5 == 0):
        print("The multiple of 5:\nBuzz")
        continue
    if(i%3 == 0 and i%5 == 0):
        print("The multiple of both 3 and 5:\nFizzBuzz")
        continue
    else:
        print(i)