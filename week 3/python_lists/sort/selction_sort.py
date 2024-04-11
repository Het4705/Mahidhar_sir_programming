def selectionSort(arr):
   

    for i in range(len(arr)):
        min=arr[i]
        index=i
        for j in range(i+1,len(arr)):
            if(arr[j]<min):
                min=arr[j]
                index=j
        arr[i],arr[index]=arr[index],arr[i]
        print(arr)

x=[5,34,2,1,0,3,4]
selectionSort(x)

        
            












































