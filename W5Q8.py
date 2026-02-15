text = str(input("Enter a string: "))
words = text.split()
revword = []

for x in words:
    temp = list(x)
    temp.reverse()
    newword = ""
        
    for i in temp:
        newword += i
        
    revword.append(newword)

newtext = ""
for x in revword:
    newtext += x + " "
    
print(newtext)