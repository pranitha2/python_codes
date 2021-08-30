def fun(l):
    l1=[]
    s1=""
    for i in range(len(l)):
        a=l.count(l[i])
        if(a%2==1):
            if l[i] not in s1:
                s1+=l[i]
    return s1
l=input()
print(fun(l))