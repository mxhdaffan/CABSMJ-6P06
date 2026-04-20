def lookup(records, item):
    for k,v in emp.items():
        if(v==src):
            return k
    return "Employee does not exist!"

emp = {"Affan":246, "Saud":308, "Abdullah":281, "Asad":349, "Abdul":479, "AlQama":635}

src = int(input("Enter a badge ID to search: "))
print("Name: ", lookup(emp,src))