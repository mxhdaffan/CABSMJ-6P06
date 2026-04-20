import math

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if ((a + b <= c) or (a + c <= b) or (b + c <= a)):
    print("Invalid triangle")
else:
    if a == b == c:
        t_type = "Equilateral"
    elif a == b or b == c or a == c:
        t_type = "Isosceles"
    else:
        t_type = "Scalene"

    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"\nArea of trianlge = {area}\nType = {t_type}")