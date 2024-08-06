n = 10
m = 20

for a in range(1,n+1):
    for b in range(1,m+1):
        if (a==1 or a==n):
            print("*" ,end='')
        elif (b==1 or b==m):
            print("*",end='')
        else:
            print(" ",end='')
    print()

            
        