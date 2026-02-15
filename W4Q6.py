def isPerfect(num):
    sumf = 0

    for i in range(1, num):
        if(num%i==0):
            sumf += i
    
    if(sumf==num):
        return True
    else:
        return False

num = int(input("Enter a number: "))

if(num <= 0):
    print("Invalid input!")
else:
    if(isPerfect(num)):
        print("\nPerfect number")
    else:
        print("\nNOT a perfect number")