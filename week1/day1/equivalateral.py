n=int(input("Enter num"))
for i in range(0,n):
    for s in range(0,n-i):
        print(" ",end="")
    for t in range(0,(i*2)+1):
        print("*",end="")
    print()