#Program to convert decimal number to binary and octal system.

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