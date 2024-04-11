class A:
    
    def fun(self):
        print("f1")
class B:
    def fun(self):
        print("f2")

class C(A,B): #* it will be following Left to Right inheritance 
    pass

ob=C()
ob.fun()   #& A's fun will be followed 