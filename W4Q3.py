import math

def effectiveArea(outer, inner):
    area = (math.pi)*((outer**2) - (inner**2))
    return area

outer = float(input("Enter outer radius (R): "))
inner = float(input("Enter inner radius (r): "))

if(outer<=0 or inner<=0):
    print("Radius can not be <= 0")
else:
    if(outer > inner):
        res = effectiveArea(outer, inner)
        print("\nEffective area = ", res)
    else:
        print("\nInvalid Radius values!")