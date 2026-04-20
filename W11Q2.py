text = input("Enter a string: ")
text = text.lower()

freq = {}
for x in text:
    if(x in freq):
        freq[x] += 1
    else:
        freq[x] = 1
        
print(freq)