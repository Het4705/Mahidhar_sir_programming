
def Eval(val1,operator,val2):
    if(operator=='+'):
        res=int(val1)+int(val2)
        return res
    elif(operator=='/'):
        res=int(val1)/int(val2)
        return res
    elif(operator=='-'):
        res=int(val1)-int(val2)
        return res
    elif(operator=='*'):
        res=int(val1)*int(val2)
        return res
    elif(operator=='%'):
        res=int(val1)%int(val2)
        return res
    elif(operator=='^'):
        res=int(val1)**int(val2)
        return res

    
    

stack=list()
exp=input("Enter")[::-1]
for i in exp:
    if i.isalnum() :
        stack.append(i)
        print(stack)
    else:
        res=Eval(stack[-2],i,stack[-1])
        stack.pop()
        stack.pop()
        stack.append(res)
print(stack[0])
    