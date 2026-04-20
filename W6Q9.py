def isConsecutive(arr):
    size = len(arr)
    
    for i in range(1, size):
        if(arr[i] == arr[i-1]+1):
            continue
        else:
            return False
        
    return True

size = int(input("Enter size: "))
arr = []

for i in range(size):
    temp = int(input(f"Enter number {i+1}: "))
    arr.append(temp)
    
arr.sort()
if(isConsecutive(arr)):
    print("This list is consecutive")
else:
    print("This list is NOT consecutive")