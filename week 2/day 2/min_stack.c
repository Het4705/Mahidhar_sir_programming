#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *below;
};

struct minStack
{
    struct Node *minStackTop;
    struct Node *stackTop;
};

void push(struct minStack *s, int data)
{
    struct Node* new1=(struct Node*)malloc(sizeof(struct Node));
    if(!new1)
    {
        printf("overflow");
        return;
    }
    new1->data=data;
    new1->below=s->stackTop->below;
    s->stackTop=new1;
    if (!s->minStackTop || s->minStackTop->data>data)
    {
       struct Node* new2=(struct Node*)malloc(sizeof(struct Node));
       new2->data=data;
       new2->below=s->minStackTop->below;
       s->minStackTop=new2;
    }    
}


void pop(struct minStack *s)
{
    if (!s->stackTop)
    {
        printf("underflow");
        return;
    }
    struct Node *temp = s->stackTop;
    if (s->minStackTop->data==temp->data)
    {
        struct Node *temp2=s->minStackTop;
        s->minStackTop=s->minStackTop->below;
        free(temp2);
    }
    s->stackTop=s->stackTop->below;
    free(temp);
}

void display(struct minStack s)
{
    struct Node *temp = s.stackTop;
    while (temp)
    {
        printf("%d\n", temp->data);
        temp = temp->below;
    }
    printf("_______\n");
}

int main()
{
    struct minStack s;
    push(&s, 3);
    push(&s, 4);
    push(&s, 1);
    push(&s, 7);
    push(&s, 0);

    display(s);

    return 0;
}
