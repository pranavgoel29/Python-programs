name = input("Enter your name: ")
reg_no = input("Registration number: ")

print(name,"\n",reg_no, "\n")

data = 1
print("Data type: ", type(data))

 
def decToOct(n):
    print(oct(n));

if __name__ == '__main__':

    n = int(input("Enter the decimal number: "))
    decToOct(n);

def decToBin(n):
    print(bin(n));

if __name__ == '__main__':
    
    n = int(input("Enter the decimal number for binary: "))
    decToBin(n);