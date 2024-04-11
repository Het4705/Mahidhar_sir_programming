#include<stdio.h>
#include<stdlib.h>



void main()
{
    char *ptr=malloc(sizeof(int)*5);
    ptr[0]=1;
    ptr[2]=3;
    printf("%d %d",*ptr,*ptr+1);


}