r1 = int(input("Enter starting point: "))
r2 = int(input("Enter stopping point: "))

if(r1>=r2):
    print("Enter suitable values!")
else:
    arr = []
    for i in range(r1, r2+1):
        arr.append(i)

    print(arr)