text = str(input("Enter a string: "))
size = len(text)

uc, lc = 0, 0
for x in text:
    if(x.isalpha()):
        if(x.isupper()):
            uc += 1
        elif(x.islower()):
            lc += 1

print(f"Uppercase Letters = {uc}\nLowercase Letters = {lc}")
