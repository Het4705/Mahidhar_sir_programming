#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node *next;
};
typedef struct node List;

void append(List *head, int data)
{
    List *ptr = (List *)malloc(sizeof(List));
    if (!ptr)
    {
        printf("\n no space available for list \n");
        return;
    }
    ptr->data = data;
    ptr->next = NULL;
    if (!head)
    {

        head = ptr;
        return;
    }
    else
    {
        List *temp = head;
        while (temp->next)
        {
            temp = temp->next;
        }
        temp->next = ptr;
    }
}

void display(List *head)
{
    if(!head)
    {
        printf("\n list not initialized");
    }
    List *temp = head;
    while (temp)
    {
        printf("%d ",temp->data);
        temp=temp->next;
    }
    printf("\n");
}
