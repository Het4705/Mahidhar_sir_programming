#include <stdio.h>

typedef struct
{
    int maxHeap[10];
    // int len=0;     this  will give error as in c we can't give values to in
    int len;
} maxHeap;

void display(maxHeap h)
{
    for (int i = 0; i < h.len; i++)
    {
        printf("%d ", h.maxHeap[i]);
    }
    printf("\n");
}

void maxHeapInsert(maxHeap *a, int data) // we need to pass address as it needs
{
    // printf("size:%d\n", (sizeof(a->maxHeap) / sizeof(a->maxHeap[0])));
    // printf("len:%d \n", a->len);
    if (a->len >= (sizeof(a->maxHeap) / sizeof(a->maxHeap[0])))
    {
        printf("Size is full\n");
        return;
    }
    if (a->len == 0)
    {
        a->maxHeap[0] = data;
        a->len++;
    }
    else
    {
        // printf("Inside ELSe\n");
        int current = a->len;
        a->maxHeap[current] = data;
        a->len++;
        int parent = (current - 1) / 2;
        while (a->maxHeap[parent] < a->maxHeap[current])
        {
            int temp = a->maxHeap[current];
            a->maxHeap[current] = a->maxHeap[parent];
            a->maxHeap[parent] = temp;
            current = parent;
            parent = (current - 1) / 2;
        }
    }
    // printf("len:%d \n", a->len);
    display(*a);
}
void maxHeapDelete(maxHeap *a)
{
    if (a->len==0)
    {
       printf("maxHeap is empty");
    }
    
    a->maxHeap[0] = a->maxHeap[a->len - 1];
    a->len--;
    int current = 0;
    int left = (current) * 2 + 1;
    int right = (current) * 2 + 2;
    while (left < a->len || right < a->len)
    {
    printf("at delete:");display(*a);
        int max=0;
        if (left < a->len && right < a->len)
        {
        printf("at 1\n");
            max = a->maxHeap[left] > a->maxHeap[right] ? left : right;
            
        }
        else if (left < a->len && right >= a->len)
        {
        printf("at 2\n");
            max = left;
        }
        else if (right < a->len && left >= a->len)
        {
        printf("at 3\n");
            max = right;
        }
        printf("m=%d ",max);
        printf("c=%d\n",current);
        if (a->maxHeap[max] > a->maxHeap[current])
        {
            printf("max=%d ",a->maxHeap[max]);
            printf("cur=%d \n",a->maxHeap[current]);
          
            int temp = a->maxHeap[max];
            a->maxHeap[max] = a->maxHeap[current];
            a->maxHeap[current] = temp;
            current = max;
            left = (current) * 2 + 1;
            right = (current) * 2 + 2;
        }
        else{
            return;
        }
    }
    printf("After Delete:");
    display(*a);
}

void main()
{
    maxHeap h;
    h.len = 0;
    maxHeapInsert(&h, 10);
    maxHeapInsert(&h, 4);
    maxHeapInsert(&h, 15);
    maxHeapInsert(&h, 16);
    maxHeapInsert(&h, 3);
    maxHeapInsert(&h, 7);
    maxHeapDelete(&h);
    maxHeapDelete(&h);
    maxHeapDelete(&h);
    maxHeapInsert(&h, 8);
}