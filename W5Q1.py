import math

def largest(*nums):
    maxn = nums[0]

    for x in nums:
        if(x > maxn):
            maxn = x

    print("\nMax Number = ", maxn)

def volume(choice):
    match choice:
        case 1:
            rad = float(input("\nEnter radius of cylinder: "))
            hgt = float(input("Enter height of cylinder: "))
            vol = (math.pi)*(rad**2)*(hgt)
        case 2:
            side = float(input("\nEnter side of the cube: "))
            vol = (side**3)
        case 3:
            lnt = float(input("\nEnter length of the cuboid: "))
            wid = float(input("Enter width of the cuboid: "))
            hgt = float(input("Enter height of the cuboid: "))
            vol = (lnt*wid*hgt)
        case _:
            vol = -1

    return vol

def areaRect():
    lnt = float(input("\nEnter length of the rectangle: "))
    brd = float(input("Enter width of the rectangle: "))
    area = lnt*brd
    print("\nArea of rectangle = ", area)

def circumference():
    rad = float(input("\nEnter radius of the circle: "))
    peri = (math.pi)*2*(rad)
    print("\nCircumference of circle = ", peri)

def swap(x, y):
    return y, x

def pointDistance():
    x1 = int(input("\nEnter x1: "))
    y1 = int(input("Enter y1: "))

    x2 = int(input("\nEnter x2: "))
    y2 = int(input("Enter y2: "))

    p1 = [x1, y1]
    p2 = [x2, y2]

    print(f"Distance between {(x1, y1)} and {(x2, y2)} = {math.dist(p1, p2)}")

pick = int(input("Choose any ->\n1) Find the largest of 3 numbers\n2) Volume\n3) Area of Rectangle" \
"\n4) Circumference of Circle\n5) Exchange variable values\n6) Find the distance between two points\n>>> "))

match pick:
    case 1:
        a = int(input("\nEnter number 1: "))
        b = int(input("Enter number 2: "))
        c = int(input("Enter number 3: "))
        largest(a, b, c)
    case 2:
        choice = int(input("\nFind the volume of ->\n1) Cylinder\n2) Cube\n3) Rectangle\n>>> "))
        res = volume(choice)

        if(res!=-1):
            print("\nVolume = ", res)
        else:
            print("\nINVALID INPUT!")
    case 3:
        areaRect()
    case 4:
        circumference()
    case 5:
        x = int(input("\nEnter x: "))
        y = int(input("Enter y: "))
        print(f"\nInitial values ->\nX = {x}\nY = {y}")
        x, y = swap(x,y)
        print(f"\nSwapped values ->\nX = {x}\nY = {y}")
    case 6:
        pointDistance()
    case _:
        print("\nINVALID INPUT!")