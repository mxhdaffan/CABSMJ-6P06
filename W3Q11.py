import math

def isPrime(num):
    if(num<=1):
        return False
    
    for i in range(2, int(math.sqrt(num)+1)):
        if(num%i==0):
            return False
        
    return True

def firstFactor(num):
    for i in range(1, num+1):
        if(num%i==0):
            return i

num = int(input("Enter a number: "))

if(num<1):
    print("INVALID INPUT!")
else:
    if(isPrime(num)):
        print("\nThis is a prime number")
    else:
        print("\nThis is NOT a prime number!\nFirst factor = ", firstFactor(num))
