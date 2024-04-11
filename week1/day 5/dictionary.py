 #* Dictionary is -----------   key      :      Value

 #&                        Set of Keys  and   List of Values
 #^                        (key:Value) ---> Item



my_dict = {
    'Name': 'Jalebi Bai',
    'rn': 8,
    'Class': 'Dhamal',
    'Address': 'Na janne kon desh se ayi'
}


print(my_dict)
my_dict.pop('rn')
print(my_dict)
print(my_dict['Address' ])
print(my_dict.values())
# my_dict.clear()        #! clear will delete all items  

# ! Iterating values
for i in my_dict.values():
   print(i)

print()
for key, value in my_dict.items():
    print(f"{key}: {value}")
