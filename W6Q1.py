s1 = float(input("Enter score in subject 1: "))
s2 = float(input("Enter score in subject 2: "))
s3 = float(input("Enter score in subject 3: "))

high = s1
if(s1>s2 and s1>s3):
    high = s1
elif(s2>s1 and s2>s3):
    high = s2
else:
    high = s3

print("Highest Score = ", high)