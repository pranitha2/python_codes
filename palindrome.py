a=int(input("enter a number: " ))
b=a
c=0
while (a>0):
rem=a%10
c=c*10+rem
a=a//10
if(b==c ):
print("yes")
else:
print("no")
