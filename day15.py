from AdventOfCodeInputReader import AdventOfCodeInputReader
import secret
from collections import defaultdict
import heapq
from collections import defaultdict, Counter, deque

reader = AdventOfCodeInputReader(secret.get_session_id(),2021,15)
input = reader.get_input()

new_input = []

for i in input:
    new_input.append([int(x) for x in i])

R = len(new_input)
C = len(new_input[0])
DR = [-1,0,1,0]
DC = [0,1,0,-1]

def solve(n_tiles):
    D = [[None for _ in range(n_tiles*C)] for _ in range(n_tiles*R)]
    Q = [(0,0,0)]
    while Q:
        (dist,r,c) = heapq.heappop(Q)
        if r<0 or r>=n_tiles*R or c<0 or c>=n_tiles*C:
            continue

        val = new_input[r%R][c%C] + (r//R) + (c//C)
        while val > 9:
            val -= 9
        rc_cost = dist + val

        if D[r][c] is None or rc_cost < D[r][c]:
            D[r][c] = rc_cost
        else:
            continue
        if r==n_tiles*R-1 and c==n_tiles*C-1:
            break

        for d in range(4):
            rr = r+DR[d]
            cc = c+DC[d]
            heapq.heappush(Q, (D[r][c],rr,cc))
    return D[n_tiles*R-1][n_tiles*C-1] - new_input[0][0]

print(solve(1))
print(solve(5))
 
# class Graph():
 
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
 
#     def printSolution(self, dist):
#         print("Vertex tDistance from Source")
#         for node in range(self.V):
#             print(node, "t", dist[node])
 
#     # A utility function to find the vertex with
#     # minimum distance value, from the set of vertices
#     # not yet included in shortest path tree
#     def minDistance(self, dist, sptSet):
 
#         # Initialize minimum distance for next node
#         min = sys.maxsize
 
#         # Search not nearest vertex not in the
#         # shortest path tree
#         for v in range(self.V):
#             if dist[v] < min and sptSet[v] == False:
#                 min = dist[v]
#                 min_index = v
 
#         return min_index
 
#     # Function that implements Dijkstra's single source
#     # shortest path algorithm for a graph represented
#     # using adjacency matrix representation
#     def dijkstra(self, src):
 
#         dist = [sys.maxsize] * self.V
#         dist[src] = 0
#         sptSet = [False] * self.V
 
#         for cout in range(self.V):
 
#             # Pick the minimum distance vertex from
#             # the set of vertices not yet processed.
#             # u is always equal to src in first iteration
#             u = self.minDistance(dist, sptSet)
 
#             # Put the minimum distance vertex in the
#             # shortest path tree
#             sptSet[u] = True
 
#             # Update dist value of the adjacent vertices
#             # of the picked vertex only if the current
#             # distance is greater than new distance and
#             # the vertex in not in the shortest path tree
#             for v in range(self.V):
#                 if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
#                     dist[v] = dist[u] + self.graph[u][v]
 
#         self.printSolution(dist)
 
 
# # Driver program
# g = Graph(9)
# g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#            [4, 0, 8, 0, 0, 0, 0, 11, 0],
#            [0, 8, 0, 7, 0, 4, 0, 0, 2],
#            [0, 0, 7, 0, 9, 14, 0, 0, 0],
#            [0, 0, 0, 9, 0, 10, 0, 0, 0],
#            [0, 0, 4, 14, 10, 0, 2, 0, 0],
#            [0, 0, 0, 0, 0, 2, 0, 1, 6],
#            [8, 11, 0, 0, 0, 0, 1, 0, 7],
#            [0, 0, 2, 0, 0, 0, 6, 7, 0]
#            ]
 
# g.dijkstra(0)

# class Graph:
#     def __init__(self):
#         #self.V = vertices
#         self.graph = defaultdict(list)
    
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
    
#     def find_lowest_risk(self,starting,ending):
#         visited = {}
#         path = []
#         path_scores = []
#         self.find_path(starting, ending, visited, path,path_scores)
    
#     def find_path(self,u,d,visited,path,path_scores):
#         visited[u] = True
#         path.append(u)
#         path_scores.append(int(input[u[0]][u[1]]))
 
#         # current = destination
#         if u == d:
#             print(path)
#             print(sum(path_scores))
#             return
#         else:
#             temp = []
#             for i in self.graph[u]:
#                 temp.append((int(input[i[0]][i[1]]),(i[0],i[1])))    
#             temp.sort()
#             self.find_path(temp[0][1] ,d,visited,path,path_scores)
                     
#         path.pop()
#         path_scores.pop()
#         visited[u] = False

#     # def find_lowest_neighbour(self,u_list):
#     #     temp = []
#     #     for i in u_list:
#     #         temp.append((int(input[i[0]][i[1]]),(i[0],i[1])))    
#     #     temp.sort()
#     #     return temp[0][1]

# g = Graph()
# for row in range(len(input)):
#     for pos in range(len(input[row])):
#         if row != 0:
#             g.addEdge((row,pos),(row-1,pos))
#         if row != len(input) -1:
#             g.addEdge((row,pos),(row+1,pos))
#         if pos != len(input[row]) -1:
#             g.addEdge((row,pos),(row,pos+1))

# g.find_lowest_risk((0,0),(len(input)-1,len(input[0])-1))