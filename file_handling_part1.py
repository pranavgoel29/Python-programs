#Program to open and close files.

import os
os.system("cls")

myfile = open("data.txt", "r")
newfile = open("answer.txt", "w")
line = " "
while line:
    line = myfile.readline()
    if 'a' not in line:
        newfile.write(line)

myfile.close()
newfile.close()
print("Newly file created.")
newfile = open("answer.txt","r")
newfile.close()