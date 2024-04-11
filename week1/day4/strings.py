print("Jay Shree {1} Jay shree {0} Jay {2}".format("RAM","Krishna","Hanuman"))  #* Wowww

li=["abc","xyz","123"]
print("-".join(li))    #* abc-xyz-123

li=["abc","xyz","123"]
print("\n".join(li))      

print("hemlo123".isalnum())  #! Check if it's alphabet OR numeric
print("hemlo 123".isalnum())  #* Check if it's alphabet OR numeric 

#TODO split

a="Jay-Shree-Ram"
txt1=a.split("-")
print(txt1)      #?['Jay', 'Shree', 'Ram']

a="Hemlo!Worlmd!im!Het"
txt2=a.split("!",2)
print(txt2)     #^['Hemlo', 'Worlmd', 'im!Het']

a="Hemlo!Worlmd!im!Het"
txt2=a.rsplit("!",2)
print(txt2)     #^['Hemlo!Worlmd', 'im', 'Het']



#TODO Partition

a="Ramam-Raghvam&Randhiram-Rajasam"
#& initial    | partition | remaining
txt2=a.partition("&")   
print(txt2)     #*('Ramam-Raghvam', '&', 'Randhiram-Rajasam')

#!-------------------------------------------------------------------------------------------

a="Ramam-Raghvam&Randhiram-Rajasam@"
#& initial-----------------------| partition | remaining
txt2=a.partition("$")   
print(txt2)     #*('Ramam-Raghvam&Randhiram-Rajasam,'',')

#!-------------------------------------------------------------------------------------------

a="Ramam-Raghvam&Randhiram-Rajasam@"

txt2=a.partition("(")    #^it's not there in string

#& initial-----------------------| partition | remaining
print(txt2)     #*('Ramam-Raghvam', '&', 'Randhiram-Rajasam')




