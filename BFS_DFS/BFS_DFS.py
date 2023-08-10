import networkx as nx
import matplotlib.pyplot as plt

class Graph :

    def __init__(self) :
        self.graph = {}
        self.visual = []
        self.visualDFS = []
        self.visualBFS = []

    def addEdge(self, u, v) :
        self.visual.append([u,v])
        if u in self.graph :
            self.graph[u].append(v)
        else :
            self.graph[u] = [v]
        self.visited = []

    
    def BFS(self, s) :
        queue = []
        self.visited.append(s)
        queue.append(s)
        print("BFS Traversal")
        while queue :
            vert = queue.pop(0)
            self.visualBFS.append(vert)
            print(vert, end = "  ")
            for i in self.graph[vert] :
                if i not in self.visited :
                    queue.append(i)
                    self.visited.append(i)

    def DFSvisit(self, v, visited) :
        
        visited[v] = True
        print(v, end = "  ")
        self.visualDFS.append(v)
        
        for i in self.graph[v] :
            if visited[i]==False :
                self.DFSvisit(i, visited)
        

    def DFS(self) :
        print("\nDFS Traversal")
        vertices = len(self.graph)
        visited = [False]*vertices
        for i in range(vertices) :
            if visited[i]==False :
                self.DFSvisit(i, visited)
            

    def visualize(self) :
        g1 = nx.Graph()
        g1.add_edges_from(self.visual)
        nx.draw_networkx(g1)
        plt.show()
    
    def visualizeBFS(self) :
        plt.clf()
        g2 = nx.Graph()
        for i in range(len(self.visualBFS)-1) :
            g2.add_edge(self.visualBFS[i], self.visualBFS[i+1])
        nx.draw_networkx(g2)
        plt.show()

    def visualizeDFS(self) :
        plt.clf()
        g3 = nx.Graph()
        for i in range(len(self.visualDFS)-1) :
            g3.add_edge(self.visualDFS[i], self.visualDFS[i+1])
        nx.draw_networkx(g3)
        plt.show()


g = Graph()
for _ in range(int(input("Enter the number of edges : "))) :
    u, v = map(int, input('Enter the start and end vertex : ').split())
    g.addEdge(u, v)

source = int(input('Enter the source vertex : '))

g.BFS(source)
g.DFS()
    
g.visualize()

g.visualizeBFS()

g.visualizeDFS()
