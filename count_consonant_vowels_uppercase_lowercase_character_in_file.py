import os
os.system("cls")

print("Enter the Name of File: ")
fileName = str(input())

infile = open(fileName, "r")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
cons = set("b c d f g h j k l m n p q r s t v w x y z B C D F G H J K L M N P Q R S T V W X Y Z")

text = infile.read().split()


countV = 0
for V in text:
    if V in vowels:
        countV += 1

countC = 0
for C in text:
    if C in cons:
        countC += 1

# for V in text:
    
#         countV += 1

print("The number of Vowels is: ",countV,"\nThe number of consonants is: ",countC)