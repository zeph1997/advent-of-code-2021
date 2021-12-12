from AdventOfCodeInputReader import AdventOfCodeInputReader
import secret
from collections import defaultdict

reader = AdventOfCodeInputReader(secret.get_session_id(),2021,12)
input = reader.get_input()

  
# This class represents a directed graph
# using adjacency list representation
class Graph:
  
    def __init__(self,vertices):
        self.V = vertices
         
        self.graph = defaultdict(list)
        self.counter = 0
        self.two_small = False
   
    def addEdge(self, u, v):
        self.graph[u].append(v)
  

    def genAllPathsUtil(self, u, d, visited, path):
        if u == "start" or u == "end":
            visited[u] = 2
        elif u.islower():
            if u in visited:
                visited[u] += 1
                if visited[u] >= 2 and not self.two_small:
                    self.two_small = True
            else:
                visited[u] = 1
        path.append(u)
 
        # current = destination
        if u == d:
            self.counter += 1
        else:
            for i in self.graph[u]:
                if ((i not in visited or visited[i] < 1) and self.two_small) or ((i not in visited or visited[i] < 2) and not self.two_small):
                    self.printAllPathsUtil(i, d, visited, path)
                     
        path.pop()
        if u == "start":
            pass
        elif u == "end":
            visited[u] = 0
        elif u.islower():
            if u in visited:
                if visited[u] >= 2:
                    self.two_small = False
                visited[u] -= 1
            else:
                visited[u] = 0
  
    def genAllPaths(self, s, d):
        visited = {}
        path = []
        self.genAllPathsUtil(s, d, visited, path)

    def getNumOfPaths(self):
        print(self.counter)
        return self.counter

a = set()
for i in input:
    one,two = i.split("-")
    a.add(one)
    a.add(two)

g = Graph(len(a))

for i in input:
    one,two = i.split("-")
    g.addEdge(one,two)
    g.addEdge(two,one)

#print(g.graph)
g.genAllPaths("start","end")
g.getNumOfPaths()
