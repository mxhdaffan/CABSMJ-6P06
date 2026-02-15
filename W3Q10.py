import math

def isPerfectSquare(num):
    s =  int(math.sqrt(num))
    if (s**2 == num):
        return True
    else:
        return False

def isFib(num):
    t1 = isPerfectSquare((5*(num**2)) + 4)
    t2 = isPerfectSquare((5*(num**2)) - 4)

    return t1 or t2

num = int(input("Enter a number: "))

if (isFib(num)):
    print("This is a fibionacci number")
else:
    print("This is NOT a fibionacci number")
