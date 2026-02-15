num = int(input("Enter a non-negative integer: "))

if(num < 0):
    print("Invalid input!")
else:
    fact = 1
    for i in range(1, num+1):
        fact *= i
    print(f"\nFactorial of {num} is = {fact}")