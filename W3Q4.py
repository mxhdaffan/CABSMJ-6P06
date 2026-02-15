def add_bitwise(num1, num2):
    while(num2!=0):
        sum_value = num1^num2       # Adds bits without carry
        carry = (num1 & num2) << 1  # AND generates a carry if both bits are same       # Shift the carry to affect the next higher bit
        
        num1 = sum_value
        num2 = carry
    
    return num1

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

res = add_bitwise(num1, num2)

print(f"\nSum of {num1} and {num2} is = {res}")