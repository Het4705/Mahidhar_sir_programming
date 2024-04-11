def rectangle_area(l,b):
    return l*b

inp=[[1,2,3,4],[1,1,3,4]]



for i in inp:
    area=list(map(rectangle_area,inp[0],inp[1]))
#*                                  \     /
#^                                   \   /
#!                                    \ /
        #* it accepts only      iterables
print(area)
