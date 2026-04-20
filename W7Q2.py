def fib(n):
    if(n==0 or n==1):
        return n
    else:
        return fib(n-1)+fib(n-2)

terms = int(input("Enter number of terms: "))

for i in range(terms):
    print(fib(i), end="\t")