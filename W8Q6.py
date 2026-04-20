text = str(input("Enter a string: "))
freq = {}

for ch in text:
    x = ch.lower()
    
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print("\nFrequency of each character ->", freq)