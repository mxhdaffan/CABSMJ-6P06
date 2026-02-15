def swap(a, b):
    a = a^b
    b = a^b
    a = a^b
    
    return a,b

a = int(input("Enter A: "))
b = int(input("Enter B: "))

print(f"\nInitial Values ->\nA: {a}\nB: {b}")
a, b = swap(a,b)
print(f"\nSwapped Values ->\nA: {a}\nB: {b}")
