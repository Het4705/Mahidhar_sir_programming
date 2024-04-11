class Binary {
    static int count=0;
     static int bSearch(int target, int high, int low, int arr[]) {
         count+=1;
         
         if(target>arr[high] || target<arr[low])
         {
             return -1;
         }
         
         if (high >= low) {
             int mid = (high + low) / 2;
             if (arr[mid] == target) {
                 return mid;
             } else if (target > arr[mid]) {
                 return bSearch(target, high, mid + 1, arr);
             } else {
                 return bSearch(target, mid - 1, low, arr);
             }
         } else {
             return -1;
         }
     }
 
     public static void main(String[] args) {
         int[] arr = {1, 2, 3, 4, 6};
         System.out.println(bSearch(5, 4, 0, arr));
         System.out.print("bsearch is called: "+count);
         
     }
 }
 