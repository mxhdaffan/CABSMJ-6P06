def findSum(*nums):
    sumf = 0

    for x in nums:
        sumf += x

    return sumf

print(findSum(1,2,3,4,5))
print(findSum(10,20,30))
print(findSum(246,281,308,349,479,635))