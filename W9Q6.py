def BubbleSort(arr):
    size = len(arr)
    
    for p in range(1,size):
        xchgs = False
        
        for i in range(0, (size-p)):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                xchgs = True
                
        if(xchgs==False):
            return

dataPackets = list(map(int, input("Enter list of data packets: ").split()))
BubbleSort(dataPackets)
print("\nSorted List ->\n", dataPackets)