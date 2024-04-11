class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.end = None
        self.count = 0

    def display(self):
        if not self.head:
            print("list is empty")
            return
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

        # insert at back
    def append(self, data):
        n1 = Node(data)
        if(not n1):
            print("Space not available")
            return
        if(not self.head):
            self.head = n1
            self.end = n1
            self.display()
            self.count += 1
            return
        self.end.next = n1
        self.end = n1
        self.count += 1
        self.display()

    def insert(self, data, position):
        n1 = Node(data)
        if(not n1):
            print("Space not available")
            return
        if(not self.head):
            self.head = n1
            self.display()
            self.count += 1
            self.end = n1
            return

        if(position > self.count):
            self.append(data)
        elif position == 0:
            n1.next = self.head
            self.head = n1
            self.count += 1
        else:
            temp = self.head
            for i in range(position-1):
                temp = temp.next
            n1.next = temp.next
            temp.next = n1
            self.count += 1
        self.display()
    
    def linear_search(self,target):
        temp=self.head
        while(temp):
            if(temp.data==target):
                return temp
            temp=temp.next
        return "not found"
    
    def middle(self,start,last):
        slow=start
        fast=start
        while(fast is not last):
            slow=slow.next
            fast=fast.next.next
        return slow.data

    # def binary_search(self,start):
    #     fast=start.next
    #     slow=start
    #     while(fast.next is not end):
    
    #         fast=fast.next
    #     while(fast.next is not end):
    #         fast=fast.next



Singly_list = List()
while(True):
    n = int(input(
        "Enter:\n  1 to append\n  2 to insert at any pos\n  3 to display\n -1 to quit\n"))
    if(n == -1):
        break
    elif(n == 1):
        Singly_list.append(int(input("enter data")))
    elif(n == 2):
        Singly_list.insert(int(input("enter data")),
                           int(input("enter position")))
    elif(n == 3):
        Singly_list.display()
    elif(n==4):
        print(Singly_list.middle(Singly_list.head,Singly_list.end))

    else:
        print("Invalid Input")
