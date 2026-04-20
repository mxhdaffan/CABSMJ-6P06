def addOnlyDigits(arr):
    sum_e = 0
    for x in arr:
        if(isinstance(x, int)):
            sum_e += x
    
    return sum_e

list1 = [1, 2.5, 3, -4]
list2 = [10, -5, 20]
        
print("Sum of only integers = ", addOnlyDigits(list1))
print("Sum of only integers = ", addOnlyDigits(list2))