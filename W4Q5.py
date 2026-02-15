num = int(input("Enter a number: "))

if(num < 0):
    print("Invalid input!")
else:
    sumd, temp = 0, num

    while(temp > 0):
        lsd = temp%10
        sumd += lsd
        temp = temp//10

    print("\nSum of digits = ", sumd)
