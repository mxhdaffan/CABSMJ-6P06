def BubbleSort(arr, size):
    for p in range(1, size):
        xchgs = False
        
        for i in range(0, (size-p)):
            if(len(arr[i]) > len(arr[i+1])):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                xchgs = True
                
        if xchgs==False:
            return

arr = list(map(str, input("Enter filenames: ").split()))
size = len(arr)

# arr.sort(key=len)
BubbleSort(arr,size)

print("\nLength Sorted Filenames ->\n", arr)