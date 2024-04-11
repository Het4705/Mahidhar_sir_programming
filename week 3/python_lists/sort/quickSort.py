def quickSort(arr,low,high):
    print(f"l:{low} h:{high}")
    if(low<high):
        pivot=arr[low]
        p=low+1
        q=high
        while(p<q):
            while( p<=high and arr[p]<pivot ):         #*       
                p+=1
            print("p:",p)
            while(arr[q]>pivot ):
                q-=1
            print("q:",q)
            if(q>p):
                arr[p],arr[q]=arr[q],arr[p]
        if(p>q):
           arr[low],arr[q]=arr[q],arr[low]
        for i in range(low,high+1):
            print(arr[i],end="")
        print()
        quickSort(arr,low,q-1)
        quickSort(arr,q+1,high)
    return


#* if crossover point happens we swap q with pivot
x=[4,5,8,2,3]
quickSort(x,0,len(x)-1)
print(x) 