import math

def isPrime(num):
    if(num<=1):
        return False
    
    for i in range(2, int(math.sqrt(num)+1)):
        if(num%i==0):
            return False
    
    return True

num = int(input("Enter a number: "))

if(num < 0):
    print("Invalid input!")
else:
    if(isPrime(num)):
        print("\nPrime number")
    else:
        print("\nNOT a prime number")
