size = int(input("Enter number of IDs: "))
arr = []
low, high = [], []

for i in range(size):
    temp = int(input(f"Enter ID {i+1}: "))
    arr.append(temp)
    
    if(arr[i]%2==0):
        low.append(arr[i])    
    else:
        high.append(arr[i])
        
print("\nLow Priority ID List -> ", low)
print("\nHigh Priority ID List -> ", high)