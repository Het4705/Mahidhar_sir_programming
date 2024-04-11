
s={1,2,-3,4,-5,-6,7,"Sdsd",(0,2,34,4,-5,-6,-2),
   "sss",0,True,False}
print(s)
g={True,-1,8,41,-5,-6,7,1}                       

#^ print(g)
#! s.add(10)                                   
#* print(s)

for i in g:
    print(i)                                                 

#! remove value
g.discard(True)   
g.remove(True)    #*Rasies Error
print(g)