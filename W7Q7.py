def reverse(num):
    rev, temp = 0, num
    
    while(temp>0):
        lsd = temp%10
        rev = (rev*10)+lsd
        temp = temp//10
        
    return rev

num = int(input("Enter a number: "))
rev = reverse(num)

if(rev==num):
    print("This is a palindrome")
else:
    print("This is NOT a palindrome")