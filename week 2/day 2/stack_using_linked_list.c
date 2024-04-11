#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* below;
};

struct Stack{
	struct Node *top;
};

void push(struct Stack *s,int data)
{
	struct Node* new1=(struct Node*)malloc(sizeof(struct Node));
    if(!new1)
    {
        printf("overflow");
        return;
    }
	new1->data=data;
	new1->below=s->top;
	s->top=new1;
}

void pop(struct Stack *s)
{
    if(!s)
    {
        printf("underflow");
        return;
    }
	struct Node* temp=s->top;
    s->top=temp->below;
    free(temp);
	
}

void display(struct Stack s)
{
	struct Node* temp=s.top;
	while(temp){
		printf("%d\n",temp->data);
		temp=temp->below;
	}
	printf("_______\n");
}



int main() {
    struct Stack s;
    push(&s,10);
    push(&s,20);
    push(&s,30);
    display(s);
    pop(&s);
    display(s);

    return 0;
}
