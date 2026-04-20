s1 = set(map(str, input("Enter IP Address list 1: ").split())) 
s2 = set(map(str, input("Enter IP Address list 2: ").split()))
    
print("\nUnique IP Addresses ->\n", s1 & s2)