def insertionSort(arr):
    if(len(arr)<2):
        return
    for i in range(1,len(arr)):
        
        for j in range(i,0,-1):
            if(arr[j]<arr[j-1]):
                arr[j],arr[j-1]=arr[j-1],arr[j]
        print(arr)

x=[5,34,2,1,0,3,4]
print(insertionSort(x),x)