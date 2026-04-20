yr = int(input("Enter a year: "))

if(yr<0):
    print("INVALID INPUT")
else:
    if((yr%4==0 and yr%100!=0) or (yr%400==0)):
        print("This is a leap year")
    else:
        print("This is NOT a leap year")