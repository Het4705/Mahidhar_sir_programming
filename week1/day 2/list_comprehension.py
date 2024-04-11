x = int(input("enter Something"))
y = int(input("enter Something"))
z = int(input("enter Something"))
n = int(input("enter Something"))
    
List=list()

List=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range (z+1) if (i+j+k)!=n]
print(List)