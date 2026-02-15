import math

a, b, c, d, e, f = 3, 2, 6, 1, 4, 7
x = int(input("Enter the value of x: "))
exp = (a*(x**5)) + (b*(x**4)) + (c*(x**3)) + (d*(x**2)) + (e*(x)) + (math.sqrt(f))
print("\nResult = ", exp)
