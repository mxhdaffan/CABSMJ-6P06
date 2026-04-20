def BinarySearch(arr, low, high, key):
    if(low>high):
        return -1
    
    mid = (low+high)//2

    if(arr[mid]==key):
        return mid
    elif(arr[mid] > key):
        return BinarySearch(arr,low,mid-1,key)
    else:
        return BinarySearch(arr,mid+1,high,key)

ids = list(map(int, input("Enter a sorted list of IDs: ").split()))

book = int(input("Enter the book ID to search: "))
res = BinarySearch(ids, 0, len(ids)-1, book)

if(res!=-1):
    print("Book found at index ", res)
else:
    print("Book not found!")