class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None


def print(head):
    ptr=head
    while(ptr):
        print(ptr.data)
        ptr=ptr.next
    
    

    



head=None
node1=Node(10)
head=node1
node2=Node(20)
node3=Node(30)

node1.next=node2
node2.next=node3
node3.next=None




