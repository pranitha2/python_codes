def zero(t):

    n = len(t)

    c = 0

    for i in range(0, n):

        if t[i] != 0:

            a = t[i]

            t[i] = t[c]

            t[c] = a

            c += 1

n = int(input("enter n: "))

l1 = []

print("enter the values one by one") 
for i in range(0, n):
    l1.append(int(input()))
    
zero(l1)
print(l1)

