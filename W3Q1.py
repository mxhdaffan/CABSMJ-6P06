size = int(input("Enter N: "))
arr = []

if(size<=0):
    print("INVALID INPUT!")
else:
    sume, prod = 0, 1

    for i in range(size):
        temp = int(input(f"Enter number {i+1}: "))
        arr.append(temp)
        sume += arr[i]
        prod *= arr[i]

    avg = sume/size
    print(f"Sum = {sume}\nProduct = {prod}\nAverage = {avg}")

