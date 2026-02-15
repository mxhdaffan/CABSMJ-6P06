def factorial(x):
    fact = 1
    
    for i in range(1, x+1):
        fact = fact*i
        
    return fact

num = int(input("Enter a non-negative integer: "))

if(num<0):
    print("INVALID INPUT!")
else:
    print(f"\nFactorial of {num} = {factorial(num)}")
