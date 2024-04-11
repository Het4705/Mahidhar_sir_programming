from queue import PriorityQueue

# & Implementation of Weighted + Directed Graph


class Edge:
    def __init__(self) -> None:
        self.weight = None
        self.destinationVertexId = None

    def getWeight(self):
        return self.weight

    def getDestinationVertexID(self):
        return self.destinationVertexId

    def setWeight(self, weight):
        self.weight = weight

    def setDestinationVertexID(self, vid):
        self.destinationVertexId = vid


class Vertex:
    def __init__(self) -> None:
        self.vertexName = ""
        self.vertexId = ""
        self.Edges = list()

    def getVertexName(self):
        return self.vertexName

    def getVertexID(self):
        return self.vertexId

    def getEdges(self):
        return self.Edges

    def setVertexName(self, vertexName):
        self.vertexName = vertexName

    def setVertexID(self, vertexId):
        self.vertexId = vertexId


class Graph:
    def __init__(self) -> None:
        self.Vertices = list()

    def display(self):
        for vertex in self.Vertices:
            print(
                f"VertexID:{vertex.getVertexID()}\nName:{vertex.getVertexName()}\nEdges->", end="{ ")
            for Edge in vertex.Edges:
                print(
                    f"({Edge.getDestinationVertexID()},{Edge.getWeight()})", end=" ")
            print(" }\n")

    def bfs(self):
        if(len(self.Vertices) < 0):
            return
        queue = list()  # using it as a queue
        visited = dict()
        visited[self.Vertices[0]] = 1  # storing Vertice objects
        queue.append(self.Vertices[0])
        while(len(queue) > 0):
            curr = queue[0]
            queue.pop()
            if curr not in visited:
                print(f"{curr.getVertexID()}")
                visited[curr] = 1
                for edge in curr.getEdges():
                    queue.append(self.getVertex(edge.getDestinationVertexID()))
               
    def checkVertexExist(self, vid):
        for v in self.Vertices:
            if(v.getVertexID() == vid):
                return True
        return False

    def getVertex(self, vid):
        for v in self.Vertices:
            if(v.getVertexID() == vid):
                return v
        return False

    def addVertex(self):
        v = Vertex()
        vid = input("Enter id of vertex:")
        while(self.checkVertexExist(vid) and len(self.Vertices) > 0):
            print("Same Id Vertex is already there please change")
            vid = input("Enter id of vertex:")
        vertexName = input("Enter Name of vertex:")
        v.setVertexID(vid)
        v.setVertexName(vertexName)
        self.Vertices.append(v)

    def addEdge(self):
        sourceVertexId = input("Enter Source ID:")
        destinationVertexId = input("Enter Vertex ID:")
        weight = int(input("Enter Weight of Edge:"))
        if not self.checkVertexExist(sourceVertexId):
            print("source Vertex doesn't exist")
            return
        if not self.checkVertexExist(destinationVertexId):
            print("destination Vertex doesn't exist")
            return
        e = Edge()
        e.setDestinationVertexID(destinationVertexId)
        e.setWeight(weight)
        self.getVertex(sourceVertexId).getEdges().append(e)

        '''
            for undirected graph '''

        e = Edge()
        e.setDestinationVertexID(sourceVertexId)
        e.setWeight(weight)
        self.getVertex(destinationVertexId).getEdges().append(e)

    def deleteEdge(self):
        sourceVertexId = input("Enter Source ID:")
        destinationVertexId = input("Enter Vertex ID:")
        if not self.checkVertexExist(sourceVertexId):
            print("source Vertex doesn't exist")
            return
        if not self.checkVertexExist(destinationVertexId):
            print("destination Vertex doesn't exist")
            return
        edges = self.getVertex(sourceVertexId).getEdges()
        for edge in edges:
            if edge.getDestinationVertexID() == destinationVertexId:
                edges.remove(edge)
        else:
            print("No such connection is there")

    def checkVisited(self, pairs, vid):
        for item in pairs:
            if(vid == item[0]):
                return True
        return False

    def prims_algo(self):
        if(len(self.Vertices) == 0):
            print("Graph not created")
            return
        pq = PriorityQueue()
        visited = list()
        mst_weight = 0

        #^ for very first Vertex
        v = self.Vertices[0]
        visited.append((v.getVertexID(), 0))
        for edge in v.getEdges():
            dId = edge.getDestinationVertexID()
            if(dId == v.getVertexID()):
                continue
            weight = edge.getWeight()
            #* priority will be assigned on the basis of smallest weight
            pq.put((weight, dId))

        while not pq.empty():
            wvPair = pq.get()
            print(f"for Pair: {wvPair}")
            v = self.getVertex(wvPair[1])

            vid = v.getVertexID()
            if(not self.checkVisited(visited, vid)):
                mst_weight += wvPair[0]
                visited.append((vid, wvPair[0]))
                for edge in v.getEdges():
                    dId = edge.getDestinationVertexID()
                    weight = edge.getWeight()
                    pq.put((weight, dId))
        print(f"Mst Follows Order:{visited}")
        print(f"Weight:{mst_weight}")

    def kruskal_algo(self):
        visited=list()
        pq=PriorityQueue()
        mst=list()
        mst_weight=0
        for vertex in self.Vertices:
            for edge in vertex.Edges:
                pq.put(edge.getWeight(),vertex.getVertexID(),edge.getDestinationVertexID)
        while not pq.empty():
            item=pq.get()
            print(item)
            # if(item[2] not in visited):
            #     mst
            #     mst_weight+=item[0]
            #     visited.append(item[1])
