def BubbleSort(arr, size):
    for p in range(1, size):
        xchgs = False

        for i in range(0, size-p):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                xchgs = True

        if(xchgs==False):
            return

arr = list(map(int, input("Enter a list: ").split()))
size = len(arr)

print("Original List -> ", arr)
BubbleSort(arr, size)
print("Sorted List -> ", arr)

if(size<2):
    print("No second largest element")
else:
    print("Second largest element: ", arr[size-2])