stop = int(input("Enter the end point of the range: "))

arr = [(x,5*(x**3)) for x in range(1,stop+1)]
print("\nGenerated List ->\n", arr)