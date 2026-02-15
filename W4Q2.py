import math

def sphereVolume(rad):
    return (4/3)*(math.pi)*(rad**3)

radius = float(input("Enter the radius of the sphere (in cm): "))
if(radius <= 0):
    print("INVALID RADIUS!")
else:
    res = sphereVolume(radius)
    print(f"\nVolume of spherical container = {res:.4f} cm^3")
