import time
for x in range(4,11):

    if(x%2==0):
        x+=1
    for i in range(1,x+1):
        if(i==1):
            print("*",end="")
           
            print(" "*(x-2),end="")
           
            print("* "*(x//2+1))
           
        if(i<x//2):
            print("*",end="")
           
            print(" "*(x-2),end="")
           
            print("* ")
           
        if(i==x//2):
            print("* "*x)
           
        if(i>x//2 and i<x-1):
            print(" "*(x-1),end="")
           
            print("*",end="")
           
            print(" "*(x-2),end="")
           
            print("*")
           
        if(i==x-1):
            print("* "*(x//2+1),end="")
           
            print(" "*(x-3),end="")
           
            print("*")
           
       

            
    print()
    print()