 #^ Filter separate the values according to function passed and a iterable

l=[1,2,-3,4,-8,-9,19]

x=tuple(filter(lambda x:x>0,l))   #* ---> gives back filtered value
print(x)

#& WAP to select only those fruits which have e in them

def func(fruits):
    for i in fruits:
        if 'e' in i:

            return fruits

fruit=["banana","Apple","Grape","Melon","SitaFal","raspberry"]

l2=set(filter(func,fruit))
l3=set(filter(lambda x:'e' not in x,fruit))
print(l2)
print(l3)