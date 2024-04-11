def findMax(arr):
    m = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if(arr[i] > m):
            m = arr[i]
            index = i
    # print(m,index)
    return m, index


def maxRobbed(arr):
    x = len(arr)-1
    index_list = list()
    sum = 0
    for i in range(x+1):
        m = findMax(arr)
        if ((m[1]+1) not in index_list and (m[1]-1) not in index_list):

            if (m[1] == 0 and x in index_list):
                arr[m[1]] = -1
                # print("else:",arr)
            elif (m[1] == x and 0 in index_list):
                arr[m[1]] = -1
                #  print("else:",arr)
            else:
                sum += m[0]
                index_list.append(m[1])
                arr[m[1]] = -1
            #   print(arr)
        else:
            arr[m[1]] = -1

        #    print("else:",arr)
# increasing index_list value by 1
    index_list = [i+1 for i in index_list]
    index_list.sort()
    return sum, index_list


# arr=[1,2,3,4,5,6,7,8,9,10]
arr = list(map(int, input().split()))

x = maxRobbed(arr)
print(x[0])
print(x[1])
