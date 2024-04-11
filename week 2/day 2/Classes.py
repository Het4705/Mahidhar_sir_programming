class Node:
    def __init__(self,data,below) -> None:
        self.value=data
        self.below=below
top=Node(None,None)
def push(data,top):
    new1=Node(data,top)
    
    top=new1
    print("Tops->",top.value)

def display(top):
    temp=top
    while(temp):
        print(temp.value,"\n|\n|")
        temp=temp.below



s0=Node(10,None)
top=s0
push(30,top)
push(40,top)
display(top)


