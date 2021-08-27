def fun(n,l):
    l1=[]
    for i in range(len(l)):
        for j in range(len(l)):
            if((l[i]+l[j])==n):
                if (l[i],l[j]) and(l[j],l[i]) not in l1:
                    l1.append((l[i],l[j]))
    return l1
n=int(input())
l=list(map(int,input().split()))
print(fun(n,l))
