a=10
print(a>>1&1)   

    #*  ex= 10 : 1010
    
        #! Right Shift divides by 2^n
    #^   Binary  | decimal | operation 
    #       1010 | 10      |  10//2^0
    #       0101 | 5       |  10//2^1
    #       0010 | 2       |  10//2^2
    #       0001 | 1       |  10//2^3
    #       0000 | 0       |  10//2^4

    #& a>>1&1  here  a>>1 returns right-shifted decimal and &1 will work for binary only hence
    #* &1 will convert that right-shifted decimal to binary  and will perfom...
    #* AND OPERATION with least bit of returned right-shifted decimal and will print it 

#^this is how it will print binary equivalent of target num by  doing a>>i&1 over a loop            
for i in range(31,-1,-1):
    print(a>>i&1,end="")