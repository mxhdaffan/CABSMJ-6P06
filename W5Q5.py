def frequency(text):
    text = text.lower()
    arr = text.split()
    
    freq = {}
    for x in arr:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
            
    return freq
    

text = str(input("Enter a string: "))
        
print(f"\nFrequency of each word in string = {frequency(text)}")
