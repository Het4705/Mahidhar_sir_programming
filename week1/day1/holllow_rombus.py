import time




for max in range(5,20):
    for i in range(1,max):
        print(" "*(max-i),end="")
        print("*",end="")
        if(i==1):
            print()
            continue
        print(" "*(2*i-3),end="")
        print("*")
        time.sleep(0.1)
    for i in range(1,max):
        print(" "*i,end="")
        print("*",end="")
        if(i==max-1):
            print()
            continue
        print(" "*(((max-i)*2)-3),end="")
        print("*")
        time.sleep(0.1)
    
    