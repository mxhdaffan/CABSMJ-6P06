s1 = set(map(str, input("Enter list of emails 1: ").split())) 
s2 = set(map(str, input("Enter list of emails 2: ").split()))
    
print("\nUnique Emails ->\n", s1 | s2)