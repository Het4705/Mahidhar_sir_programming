#include <iostream>
using namespace std;

int max_child=;

class Node{
       public:
       int data;
       Node *sibling=nullptr;
       Node *first_child=nullptr;
};

void insert_childs(Node *root)
{
    int data;
    cout<<"Enter data to enter:";
    cin>>data;
    Node *new1=new Node();
    new1->data=data;
    if(!new1)
    {
        cout<<"No Space for new Node\n";
        return ;
    }
   Node *temp_root=root;
   while(temp_root->first_child)
   {
     Node *temp=root->first_child;
     if (!temp->sibling)
     {
        temp->sibling=new1;
     }
     else  
     {
        // cout<<"Enter 0 to add %d as child of %d or 1 as a si"
     }  
   }
   else{
    root->first_child=new1;
   }


}


