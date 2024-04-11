class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BST:
    head = None

    def createBST(self):
        data = int(input("Enter data:"))
        new1 = Node(data)
        if(self.head == None):
            self.head = new1
            option = int(input("Enter 1 to add further or -1 to stop:"))
            if option == 1:
                self.createBST()
            else:
                return new1
        else:
            temp = self.head
            while(True):
                if data > temp.data:
                    if temp.right:
                        temp = temp.right
                    else:
                        temp.right = new1
                        option = int(input("Enter 1 to add further or -1 to stop:"))
                        if option == 1:
                            self.createBST()
                        else:
                            return new1
                    
