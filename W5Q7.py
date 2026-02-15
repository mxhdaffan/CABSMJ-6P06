def reverseChars(arr):
    size = len(arr)
    arr.reverse()

    text = ""
    for x in arr:
        text += x

    return text

text = str(input("Enter a sentence: "))
arr = list(text)
res = reverseChars(arr)
print(res)