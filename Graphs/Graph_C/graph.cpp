#include <iostream>
#include <vector>
#include <list>
#include <string.h>
#include <queue>
#include <iterator>
#include "readMe.h"
using namespace std;

class Edge
{
public:
    int DestinationVertexID;
    int weight;
    Edge() {}
    Edge(int destVID, int w)
    {
        DestinationVertexID = destVID;
        weight = w;
    }
    void setEdgeValues(int destVID, int w)
    {
        DestinationVertexID = destVID;
        weight = w;
    }
    int getDestinationVertexID()
    {
        return DestinationVertexID;
    }
    int getweight()
    {
        return weight;
    }
    void setDestinationVertexID(int destVID)
    {
        DestinationVertexID = destVID;
    }
    void setweight(int w)
    {
        weight = w;
    }
};

class Vertex
{
public:
    int vertex_id;
    string vertex_name;
    list<Edge> edgelist;

    Vertex()
    {
        vertex_id = 0;
        vertex_name = "";
    }
    Vertex(int id, string vname)
    {
        vertex_id = id;
        vertex_name = vname;
    }

    int getID()
    {
        return vertex_id;
    }
    string getStateName()
    {
        return vertex_name;
    }
    void setID(int id)
    {
        vertex_id = id;
    }
    void setStateName(string vname)
    {
        vertex_name = vname;
    }
    list<Edge> &getEdgeList()
    {
        return edgelist;
    }
};
class Graph
{

private:
    vector<Vertex> vertices;

public:
    void addVertex(int vid, string vname)
    {
        bool check = CheckIfVertexExsistByStateID(vid);
        if (check == false)
        {
            Vertex v(vid, vname);
            vertices.push_back(v);
            cout << "Vertex Added Successfully\n";
        }
        else
        {
            cout << "Vertex already exsist\n";
        }
    }

    bool updateVertex(int vid, string vname)
    {
        for (int i = 0; i < vertices.size(); i++)
        {
            if (vid == vertices.at(i).getID())
            {
                vertices.at(i).setID(vid);
                vertices.at(i).setStateName(vname);
                return true;
            }
        }
        return false;
    }

    void addEdge(int sourceID, int DestinationID, int weight)
    {
        if (CheckIfVertexExsistByStateID(sourceID) && CheckIfVertexExsistByStateID(DestinationID))
        {
            for (int i = 0; i < vertices.size(); i++)
            {
                if (vertices[i].getID() == sourceID)
                {
                    Edge e(DestinationID, weight);
                    vertices[i].getEdgeList().push_back(e);
                    cout << "EDge added\n";
                    break;
                }
            }
        }
        else
        {
            cout << "Either source or destination ID doesn't exsist";
        }
    }
    void deleteEdge(int sourceID, int DestinationID, int weight)
    {

        if (CheckIfVertexExsistByStateID(sourceID) && CheckIfVertexExsistByStateID(DestinationID))
        {
            for (int i = 0; i < vertices.size(); i++)
            {
                if (vertices[i].getID() == sourceID)
                {
                    list<Edge>::iterator ptr;
                    for (ptr = vertices[i].getEdgeList().begin(); ptr != vertices[i].getEdgeList().end(); ptr++)
                    {
                        if (ptr->getDestinationVertexID() == DestinationID && ptr->getweight() == weight)
                        {
                            vertices[i].getEdgeList().erase(ptr);
                            break;
                        }
                    }
                }
            }
        }

        else
        {
            cout << "Either source or destination ID doesn't exsist";
        }
    }

    bool CheckIfVertexExsistByStateID(int vid)
    {

        for (int i = 0; i < vertices.size(); i++)
        {
            if (vertices[i].vertex_id == vid)
            {

                return true;
            }
        }
        return false;
    }

    void DeleteVertex(int vid)
    {
        if (CheckIfVertexExsistByStateID(vid))
        {
            // deleting all edges to that node
            for (int i = 0; i < vertices.size(); i++)
            {

                if (!vertices.at(i).getEdgeList().empty() || vertices.at(i).getID() != vid)
                {
                    list<Edge>::iterator ptr;
                    list<Edge> newEdgeList;
                    cout << "IN :" << vid << endl;
                    for (ptr = vertices.at(i).getEdgeList().begin(); ptr != vertices.at(i).getEdgeList().end(); ptr++)
                    {
                        if (ptr->getDestinationVertexID() != vid)
                        {
                            newEdgeList.push_back(*ptr);
                        }
                    }
                    vertices.at(i).getEdgeList() = newEdgeList;
                }
            }
            for (int i = 0; i < vertices.size(); i++)
            {
                if (vertices.at(i).getID() == vid)
                {
                    vertices.erase(vertices.begin() + i);
                    break;
                }
            }
        }
        else
        {
            cout << "Vertex Doesn't Exsist\n";
        }
    }

    void print_graph()
    {
        for (int i = 0; i < vertices.size(); i++)
        {
            cout << "{" << vertices.at(i).getID() << "," << vertices.at(i).getStateName() << "}-->[ ";
            list<Edge>::iterator ptr;
            if (!vertices.at(i).getEdgeList().empty())
            {
                for (ptr = vertices.at(i).getEdgeList().begin(); ptr != vertices.at(i).getEdgeList().end(); ptr++)
                {
                    cout << "{ ";
                    cout << ptr->getweight() << "KM," << ptr->getDestinationVertexID() << "},";
                }
            }
            cout << " ]\n";
        }
    }

    void bfs()
    {
        if (vertices.empty())
        {
            cout << "Graph is Empty";
        }
        else
        {

            queue<Vertex> Queue;
            vector<vector<int>> visited(vertices.size(), vector<int>(2));
            for (int i = 0; i < vertices.size(); i++)
            {
                visited[i][0] = vertices.at(i).getID();
                visited[i][1] = 0;
            }

            Queue.push(vertices.at(0));
            cout << "\n**********  BFS  ***********\n";

            while (!Queue.empty())
            {
                Vertex v = Queue.front(); // Get the front element
                cout << "Vid:" << v.getID() << " Vname:" << v.getStateName() << endl;
                SetVisited(visited, v);

                list<Edge>::iterator ptr = v.getEdgeList().begin();

                for (ptr; ptr != v.getEdgeList().end(); ptr++)
                {
                    if (!CheckVisited(visited, v) && !inTheQueue(Queue, v))
                    {
                        Queue.push(v);
                    }
                }
            }
        }
    }

private:
    bool inTheQueue(queue<Vertex> &q, Vertex v)
    {
        queue<Vertex> temp = q;
        while (!temp.empty())
        {
            if (temp.front().getID() == v.getID())
            {
                return true;
            }
            temp.pop();
        }
        return false;
    }

    void SetVisited(vector<vector<int>> &visited, Vertex v)
    {
        for (int i = 0; i < visited.size(); i++)
        {
            if (visited[i][0] == v.getID())
            {
                visited[i][1] == 1;
            }
        }
    }

    bool CheckVisited(vector<vector<int>> &visited, Vertex v)
    {
        for (int i = 0; i < visited.size(); i++)
        {
            if (visited[i][0] == v.getID())
            {
                if (visited[i][1] == 1)
                {
                    return true;
                }
                return false;
            }
        }
        return false;
    }
};

int main()
{
    int option = -1;
    Graph g;

    do
    {

        cout << "What Operations do you want perform?\n"
             << "Select Option number .\nEnter 0 to Exit\n";
        cout << "1: Add Vertex." << endl;
        cout << "2: Update Vertex." << endl;
        cout << "3: Delete Vertex." << endl;
        cout << "4: Add Edge." << endl;
        cout << "5: Update Edge." << endl;
        cout << "6: Delete Edge." << endl;
        cout << "7: Check if 2 vertices are Neighbours." << endl;
        cout << "8: Print All Neighbours of a Vertex" << endl;
        cout << "9: Print Graph" << endl;
        cout << "10:Clear Screen " << endl;
        cout << "11:bfs " << endl;
        cout << "0:Exit Program " << endl;

        cin >> option;

        switch (option)
        {
        case 0:
            break;
        case 1:
        { // we need to provide this  bracket else it lead to string cross intializer error

            string vname;
            int vid;
            cout << "Add Vertex Operation -\n";
            cout << "Enter Vid:";
            cin >> vid;
            cout << "Enter vname:";
            cin >> vname;
            g.addVertex(vid, vname);
        }
        break;

        case 2:
        {
            cout << "Update Vertex Operation -" << endl;
            string vname;
            int vid;
            cout << "Enter Vid:";
            cin >> vid;
            cout << "Enter vname:";
            cin >> vname;
            g.updateVertex(vid, vname);
        }
        break;

        case 3:
            cout << "Delete Vertex Operation -" << endl;
            int vid;
            cout << "Enter VID:";
            cin >> vid;
            g.DeleteVertex(vid);
            break;

        case 4:
            cout << "Add Edge Operation -" << endl;
            int sourceID;
            int DestinationID;
            int weight;
            cout << "Enter Source Vertex:";
            cin >> sourceID;
            cout << "Enter Destination Vertex:";
            cin >> DestinationID;
            cout << "Enter weight:";
            cin >> weight;
            g.addEdge(sourceID, DestinationID, weight);
            break;

        case 5:
            cout << "Update Edge Operation -" << endl;
            break;

        case 6:
            cout << "Delete Edge Operation -" << endl;
            {
                int sourceID;
                int DestinationID;
                int Weight;

                cout << "Enter Source Vertex:";
                cin >> sourceID;
                cout << "Enter Destination Vertex:";
                cin >> DestinationID;
                cout << "Enter Weight:";
                cin >> Weight;
                g.deleteEdge(sourceID, DestinationID, Weight);
            }
            break;

        case 7:
            cout << "Check if 2 vertices are Neighbours -" << endl;
            break;

        case 8:
            cout << "Print All Neighbours of a Vertex -" << endl;
            break;

        case 9:
            cout << "Print  Graph -" << endl;

            g.print_graph();
            break;

        case 10:
            cout << "clear screen-" << endl;
            break;
        case 11:
            cout << "BFS\n";
            g.bfs();
            break;

        default:
            cout << "Insert proper option" << endl;
            break;
        }

    } while (option != 0);
    return 0;
}
