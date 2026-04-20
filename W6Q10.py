size = int(input("Enter an integer: "))
arr = []

for i in range(1, size+1):
    if(i%3==0 and i%5==0):
        arr.insert(i, "FizzBuzz")
    elif(i%3==0):
        arr.insert(i, "Fizz")
    elif(i%5==0):
        arr.insert(i, "Buzz")
    else:
        arr.insert(i, str(i))

print(arr)