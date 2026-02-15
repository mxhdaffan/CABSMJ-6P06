def swap(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a,b

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(f"\nInitial values ->\nA = {a}\nB = {b}")
a, b = swap(a,b)
print(f"\nNew values ->\nA = {a}\nB = {b}")
