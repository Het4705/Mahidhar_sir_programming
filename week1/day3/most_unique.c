#include <stdio.h>

void fun(int *a){
  for (int i=0;i<=sizeof(a)/sizeof(a[0]) ;i++  )
  {
    printf("%d ",a[i]);        //* both are same                           
    printf("%d ",i[a]);       //^ will give same value as a[i]
  }
}

int main()
{
   int a[3]={1,2,3};
   printf("%d",sizeof(a));
   
   fun(a);
}                       
     //! For a    