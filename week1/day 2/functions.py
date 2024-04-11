# def fun(*a):
#     print(a)
#     for i in a:
#         print(i,end="___")

# def Enrollment_generator(Initial,*numbers,endg):
#     for i in numbers:
#         print(f"{Initial}{i}{end}")

# fun(1,2,3,"@2","@sdwwd","peoe")  


# Enrollment_generator(Initial=210303105,*numbers=33,44,55,289,33,11,55,323,413, endg=5)


def fun(*a):
    print(a)
    for i in a:
        print(i, end="___")

def Enrollment_generator( *numbers,Initial):   #& here we need to give *numbers earlier 
    for i in numbers:
        print(f"{Initial}{i}")

def Enrollments( end,*numbers,Initial):   #& here we need to give *numbers earlier 
    for i in numbers:
        print(f"{Initial}{i}{end}")

fun(1, 2, 3, "@2", "@sdwwd", "peoe")

Enrollment_generator(33, 44, 55, 289, 33, 11, 55, 323, 413,Initial=210303105)
Enrollments("S",222,2323,3434,3434,Initial="yu")      
Enrollments("S",222,2323,3434,3434,end="yu")      
