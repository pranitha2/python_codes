def grid(n):
    for i in range(0,n):
        
        for j in range(i,n+i):
            
            print(chr(97+j),end="")
            
        print('')

grid(4)
