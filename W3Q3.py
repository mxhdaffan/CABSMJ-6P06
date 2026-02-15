def surfaceArea(len, brd, hgt):
    return 2*((len*brd)+(brd*hgt)*(hgt*len))
        
def volume(len, brd, hgt):
    return len*brd*hgt

len = float(input("Enter length of the cuboid: "))
brd = float(input("Enter breadth of the cuboid: "))
hgt = float(input("Enter height of the cuboid: "))

print("\nSurface Area = ", surfaceArea(len,brd,hgt))
print("Volume = ", volume(len,brd,hgt))