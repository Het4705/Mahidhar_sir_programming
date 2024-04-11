# a="12gAgTdTTWbb"
# for i in range(len(a)):
#     if  65<=ord(a[i])>=90:
#         a[i]=  ord(a[i])+32
#     elif  97<=ord(a[i])>=122:
#          a[i]= ord(a[i])-32
# print(a)
# # for i in a:
# #     print(ord(i))
# help(str)
str1="Shree Ram"
print(str1)
print(id(str1))

str1=str1.__add__(" Janki")

#^ id will change as strings are immutable hence new location will be allocated to str1 ... that is its not same
print(id(str1))             

x=10
print("id=%u" % id(x))

x=12
print("id=%u" % id(x))

print(str1)




