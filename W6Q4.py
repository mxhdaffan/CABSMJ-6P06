def days_in_month(month):
    if month == 2:
        return 28
    elif month in [4, 6, 9, 11]:  # April, June, September, November
        return 30
    else:  # January, March, May, July, August, October, December
        return 31

mon = int(input("Enter a month number: "))
print(f"Days in month {mon} = {days_in_month(mon)}")