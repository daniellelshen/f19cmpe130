import queue

class Graph():
    def __init__(self,vertices):
        self.V = vertices
        self.edges = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def minDistBFS(self, u, v):
        # visited[n] for keeping track
        # of visited node in BFS
        visited = [0] * self.V

        # Initialize distances as 0
        distance = [0] * self.V

        # queue to do BFS.
        Q = queue.Queue()
        distance[u] = 0

        Q.put(u)
        visited[u] = True
        while (not Q.empty()):
            x = Q.get()

            for i in range(len(self.edges[x])):
                if (visited[self.edges[x][i]]):
                    continue

                # update distance for i
                distance[self.edges[x][i]] = distance[x] + 1
                Q.put(self.edges[x][i])
                visited[self.edges[x][i]] = 1
        return distance[v]

    def addEdge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

# Driver  Code
if __name__ == '__main__':
    g = Graph(9)
    edges = [[] for i in range(9)]
    g.addEdge(0, 1)
    g.addEdge(0, 7)
    g.addEdge(1, 7)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(2, 5)
    g.addEdge(2, 8)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    g.addEdge(6, 7)
    g.addEdge(7, 8)

    print(g.minDistBFS(5,1))
