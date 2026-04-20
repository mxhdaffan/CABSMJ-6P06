def calculate_routes(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*calculate_routes(n-1)
    
num = int(input("Enter a non-negative integer: "))
if(num<0):
    print("INVALID INPUT!")
else:
    print(f"\nFactorial of {num} = {calculate_routes(num)}")