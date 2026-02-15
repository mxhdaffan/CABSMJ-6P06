def removeIndentation(text):
    arr = text.splitlines()
    newtxt = ""

    for x in arr:
        line = x.lstrip()
        newtxt += line + " "
        
    return newtxt

text = '''Hello
          My
          Name
          is
          Affan'''

print("\nTransformed Text ->\n", removeIndentation(text))