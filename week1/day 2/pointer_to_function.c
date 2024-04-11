#include<stdio.h>

int fun(){
      printf("hii");
      return 1;
}

void main()
{
   void (*fn_ptr)(int)=&fun;
   (*fn_ptr)(6);
}