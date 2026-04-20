def days_in_month(month, year):
    if month == 2:
        if((year%4==0 and year%100!=0) or (year%400==0)):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:  # April, June, September, November
        return 30
    else:  # January, March, May, July, August, October, December
        return 31

mon = int(input("Enter a month number: "))
yr = int(input("Enter a year: "))

if(mon<1 or mon>12 or yr<0):
    print("INVALID INPUT!")
else:
    print(f"Days in month {mon} of {yr} = {days_in_month(mon, yr)}")