s1 = float(input("Enter temperature reading from sensor 1: "))
s2 = float(input("Enter temperature reading from sensor 2: "))
s3 = float(input("Enter temperature reading from sensor 3: "))

low = s1
if(s1<s2 and s1<s3):
    low = s1
elif(s2<s1 and s2<s3):
    low = s2
else:
    low = s3

print("\nLowest Temperature Reading = ", low)