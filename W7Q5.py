rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(rows):
        if(i <= j):
            print("*", end="  ")
    
    print()