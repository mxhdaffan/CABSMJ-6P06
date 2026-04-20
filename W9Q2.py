arr = list(map(int, input("Enter a list of product IDs: ").split()))
item = int(input("Enter an item to search: "))

if(item in arr):
    print("Found")
else:
    print("Not found!")