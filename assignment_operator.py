#program to perform arithematic operations

print("Please select operation -\n" \
        "1. +=\n" \
        "2. -=\n" \
        "3. *=\n" \
        "4. /=\n")
  
  
# Take input from the user 
select = int(input("Select operations form 1, 2, 3, 4 :"))
  
num_1 = val_1 = int(input("Enter first number: "))
val_2 = int(input("Enter second number: "))

if select == 1:
    val_1+=val_2
    print(num_1, "+=", val_2, "=",val_1)

if select == 2:
    val_1-=val_2
    print(num_1, "-=", val_2, "=",val_1)

if select == 3:
    val_1*=val_2
    print(num_1, "*=", val_2, "=",val_1)

if select == 4:
    val_1/=val_2
    print(num_1, "/=", val_2, "=",val_1)