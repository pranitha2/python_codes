def grid(n):
    for i in range(0,n):
        
        for j in range(i,n+i):
            x=j;
            x%=26
            print(chr(97+x),end="")
            
        print('')

grid(-10)
