def merge(a,b):
    n, m = len(a), len(b)
    i, j = 0, 0
    c = []

    while(i<n and j<m):
        if(a[i] < b[j]):
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1

    return c + a[i:] + b[j:]

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    a = mergeSort(arr[:mid])   # left half
    b = mergeSort(arr[mid:])   # right half

    return merge(a, b)

arr = list(map(int, input("Enter a list: ").split()))

print("\nOriginal List ->\n", arr)
arr = mergeSort(arr)
print("\nSorted List ->\n", arr)

# Best Case: O(n logn)
# Average Case: O(n logn)
# Worst Case: O(n logn)