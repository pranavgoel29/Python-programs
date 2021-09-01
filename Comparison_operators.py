#program to perform arithematic operations

print("Please select operation -\n" \
        "1. >\n" \
        "2. <\n" \
        "3. ==\n" \
        "4. <=\n"\
        "5. >=\n")
  
  
# Take input from the user 
select = int(input("Select operations form 1, 2, 3, 4, 5 :"))
  
val_1 = int(input("Enter first number: "))
val_2 = int(input("Enter second number: "))

if select == 1:
    print(val_1, ">", val_2, "=",val_1>val_2)

if select == 2:
    print(val_1, "<", val_2, "=",val_1<val_2)

if select == 3:
    print(val_1, "==", val_2, "=",val_1==val_2)

if select == 4:
    print(val_1, "<=", val_2, "=",val_1<=val_2)

if select == 5:
    print(val_1, ">=", val_2, "=",val_1>=val_2)