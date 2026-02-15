text = str(input("Enter a string: "))

vow, cons = 0, 0
vowlist = []

for x in text:
    if(x.isalpha()):
        ch = x.lower()

        if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
            vow += 1
            vowlist.append(x)
        else:
            cons += 1

print(f"\nVowel Count = {vow}\nConsonant Count = {cons}")
print(f"\nVowel List -> {vowlist}")
