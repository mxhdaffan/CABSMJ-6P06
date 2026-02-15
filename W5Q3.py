def evenIndices(text):
    size = len(text)
    newtxt = ""

    for i in range(size):
        if(i%2==0):
            continue
        else:
            newtxt += text[i]

    return newtxt


text = str(input("Enter a string: "))
print("\nModified string = ", evenIndices(text))