l=['a','b','c']
str=[]
list=[]
for i in l:
    str.append(i)
    # print("at1")
    for j in l:
        str.append(j)
        # print("at2")
        for k in l:
            str.append(k)
            if(len(str)==3 ):
                # print(str)
                if(str in list):
                    pass
                else:
                    list.append(str)
                str.pop()
                # print(str)
        str.pop()
    str.pop()
for i in list:
    print(i)
            

# # print(list)
# l=[]
# k=['a','b','c']
# l.append(k)
# print(l)