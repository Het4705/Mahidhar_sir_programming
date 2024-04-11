def bSort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

x=[5,34,2,1,0,3,4]
bSort(x)
print(x)