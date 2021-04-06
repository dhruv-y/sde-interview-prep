'''
Description => Given a directed graph, design an algorithm to find out whether there 
is a route between two nodes.

Approach => Use DFS/BFS to check path between nodes. BFS (non recursive) preferred for route finding
and DFS (recursive) preferred for reaching end of tree.

'''


from collections import defaultdict

class Graph:
    def __init__(self, V=None):
        self.V = V
        self.adj = defaultdict(list)
        
    def addEdge(self,u,v):
        self.adj[u].append(v)
        
    def isReachable(self,u,v):
        visited = [False] * self.V
        queue = []
        # starting with node u
        queue.append(u)
        visited[u] = True
        
        while queue:
            node = queue.pop(0)
            
            # check if equals v
            if node == v:
                return True
            # check all neighbours of current node
            for adj in self.adj[node]:
                if not visited[adj]:
                    queue.append(adj)
                    visited[adj] = True
                    
        return False

    
if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
        
    print(g.isReachable(2, 3))