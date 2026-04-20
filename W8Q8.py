def SKU_code(text):
    size = len(text)
    if(size<4):
        return "Not Eligible!"
    else:
        newtext = text[:2]+ text[-2:]
        return newtext

text = str(input("Enter a string: "))
print(SKU_code(text))