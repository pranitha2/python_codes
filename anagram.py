str= input("enter a string:")

hl=int((len(str))/2)

s1=str[0:hl]
s2=str[hl:len(str)]
ans1=sorted(s1)
ans2=sorted(s2)
i=0
n=0
while i<len(s1):
if ans1[i]!=ans2[i]:
n=n+1
i=i+1
print(n)
