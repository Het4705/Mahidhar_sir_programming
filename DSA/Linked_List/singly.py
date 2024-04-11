class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class List:
    def __init__(self) -> None:
        self.head = None
        self.end = None

    def append(self, data):
        if(not self.head):
            self.head = Node(data)
            self.end = self.head
        else:
            self.end.next=Node(data)
            self.end=self.end.next

    def display(self):
        ptr=self.head
        while(ptr):
            print(ptr.data,end=" --> ")
            ptr=ptr.next
        print("X")

l=List()
l.append(10)
l.append(12)
l.append(14)
l.append(16)
l.append(70)
l.display()

        
    
