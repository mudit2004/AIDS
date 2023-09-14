from collections import defaultdict

class Graph :
    def __init__(self) -> None:
        self.edges = defaultdict(dict)
        self.nodes = defaultdict(int)

    def addNode(self, x, hval) :
        self.nodes[x] = hval 
    
    def addEdge(self, u, v, w) :
        self.edges[u][v] = w

    def calcCost(self, cost, path) :
        return cost-self.nodes[path[-2]] + self.edges[path[-2]][path[-1]] + self.nodes[path[-1]]
    
    def smastar(self, source, goal, bound) :

        if source==goal :
            print(source)
            return
        
        if bound==1 :
            print('Goal not found')
            return
        
        bound+=1
        
        frontier = []
        frontier.append((self.nodes[source], (source,)))

        visited = defaultdict(list)
        mem = 1

        while frontier :
            
            if mem==bound :
                frontier.pop(-1)
                mem-=1
            
            if not frontier :
                print('Failure')
                return
            
            cost, path = frontier.pop(0)
            added = False
            for i in self.edges[path[-1]] :
                if i not in visited[path[-1]] :
                    npath = path+(i,)
                    ncost = self.calcCost(cost, npath)
                    frontier.append((ncost, npath))
                    visited[path[-1]].append(i)
                    mem+=1
                    added = True
                    if mem==bound :
                        break 
                
            
            if not added :
                print('Failure')
                return
            
            frontier.sort()
            if frontier[0][1][-1]==goal :
                print('Path :', frontier[0][1])
                print('Cost :', frontier[0][0])
                return 
            


g = Graph()

for _ in range(int(input('Enter the number of nodes : '))) :
    x, hval = input('Enter the node and heuristic value : ').split()
    g.addNode(x, int(hval))
    
for _ in range(int(input('\nEnter the number of edges : '))) :
    u,v,w = input('Enter the source and destination of edge : ').split()
    g.addEdge(u,v,int(w))
    
source, goal = input('Enter the source and goal nodes : ').split()
bound = int(input('Enter memory bound : '))
g.smastar(source, goal, bound)

            
            
            
            



