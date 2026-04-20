text = "Different string Methods!"

words = text.split()
print("Words ->", words)

print("Uppercase ->", text.upper())

print("Index of substring 'rules': ", text.find("rules"))

res = 'o' in text
print("Searching for 'o': ", res)

print("Replaced string: ", text.replace('!', '?'))