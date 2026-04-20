def calculateDigits(num):
    dig, temp = 0, num
    
    while(temp>0):
        dig += 1
        temp = temp//10
        
    return dig

def isArmstrong(num):
    dig = calculateDigits(num)
    
    sumd, temp = 0, num
    while(temp>0):
        lsd = temp%10
        sumd += (lsd**dig)
        temp = temp//10
        
    if(sumd==num):
        return True
    else:
        return False
    
num = int(input("Enter a number: "))
if(isArmstrong(num)):
    print("This is a Armstrong number")
else:
    print("This is NOT a Armstrong number")