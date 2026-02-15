x = int(input("Enter x: "))
y = int(input("Enter y: "))

nume = 1 + (x/y) + (x**y)
deno = 2 + (y/x) + (y**x)

print("\nResult = ", nume/deno)
