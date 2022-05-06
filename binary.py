n=int(input("Enter a number: "))
l=[]
while(n>0):
    num=n%2
    l.append(num)
    n=n//2
l.reverse()
for i in l:
    print(i)
