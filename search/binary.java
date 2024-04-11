class binary{
    static int bSearch(int target,int high,int low,int arr[])
    {
        if(high>=low)
        {
              int mid=(high+low)/2;
              if(mid==target)
              {
                return mid;
              }
              else if(target>arr[mid])
              {
                return bSearch(target,high,mid+1,arr);
            }
            else{
                
                return bSearch(target,mid-1,low,arr);
              }
        }
        else{
            return -1;
        }
    }
    public static void main()
    {
        int []arr={1,2,3,4,5};
        System.out.println(bSearch(4,4,0,arr));
    }
}