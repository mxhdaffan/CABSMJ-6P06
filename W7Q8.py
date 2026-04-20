def merge(a, b):
    c = []

    n, m = len(a), len(b)
    i,j = 0,0

    while(i<n and j<m):
        if(a[i] < b[j]):
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1

    c.extend(a[i:])
    c.extend(b[j:])

    return c

l1 = list(map(int, input("Enter list 1: ").split()))
l2 = list(map(int, input("Enter list 2: ").split()))

l3 = merge(l1, l2)

print("List 1 ->", l1)
print("List 2 ->", l2)
print("List 3 ->", l3)