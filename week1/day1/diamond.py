for i in range(0,5):
    for j in range(0,5):
        if(i+j==(5//2) or i+j==(3*5)//2-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
