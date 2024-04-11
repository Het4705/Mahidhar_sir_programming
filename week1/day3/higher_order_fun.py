def fun1():
    print("fun1")
    def fun2():
        print("fun2")
        def fun3():
            print("fun3")
        return fun3
    
    #! fun2() i can call it from here     
    return fun2


a=fun1()    #* as fun1 returns address of fun2 it will be stored in fun1
b=a()    #* as a stores address of fun2 on calling it , it will return address of fun3
b()

#& WE can do
print("Another MEthod")
fun1()()()

#*    A function can be called higher order function when a function return another function 
#*    or function accepts a function as a Argument

