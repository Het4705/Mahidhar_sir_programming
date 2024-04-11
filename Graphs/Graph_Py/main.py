from graph import Graph

g=Graph()

while True:
    option=(input("Enter\n1:Add Vertex\n2:Add Edge\n3:Add display\n"
                     "4:Delete Edge\n"
                     "5:Prims\n"
                     "6:BFS\n"
                     "-1:Quit:"))
    if(option=="1"):
        g.addVertex()
    elif(option=="2"):   #^ here i have datatype of option as String 
        g.addEdge()      #^ other wise for int if i give any random input like
    elif(option=="3"):   #* Falana Dhikna then it will not go to default else and will raise 
        g.display()      #& Type Error
    elif(option=="4"):
        g.deleteEdge()
    elif(option=="5"):
        g.primsAlgo()
    elif(option=="5"):
        g.primsAlgo()
    elif(option=="6"):
        g.bfs()
    elif(option=="-1"):
        exit()
    else:
        print("Please Select Valid Option")
        
    

