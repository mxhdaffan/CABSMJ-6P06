def find_signal_sync(a, b):
    r = a%b
    while(r!=0):
        a = b
        b = r
        r = a%b
    
    return b

a = int(input("Enter signal A: "))
b = int(input("Enter signal B: "))
gcd = find_signal_sync(a,b)
print(f"\nGCD of {a} and {b} is = {gcd}")