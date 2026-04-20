def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    
    a = [x for x in arr[1:] if x <= pivot]
    b = [x for x in arr[1:] if x > pivot]

    return quickSort(a) + [pivot] + quickSort(b)

arr = list(map(int, input("Enter a list: ").split()))

print("\nOriginal List ->\n", arr)
arr = quickSort(arr)
print("\nSorted List ->\n", arr)

# Best Case: O(n logn)
# Average Case: O(n logn)
# Worst Case: O(n^2)