from AdventOfCodeInputReader import AdventOfCodeInputReader
import secret


reader = AdventOfCodeInputReader(secret.get_session_id(),2021,12)
input = reader.get_input()

from collections import defaultdict
  
# This class represents a directed graph
# using adjacency list representation
class Graph:
  
    def __init__(self,vertices):
        # No. of vertices
        self.V = vertices
         
        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.counter = 0
        self.two_small = False
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
  
    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, u, d, visited, path):
 
        # Mark the current node as visited and store in path
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
 
        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            #print(path)
            self.counter += 1
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if ((i not in visited or visited[i] < 1) and self.two_small) or ((i not in visited or visited[i] < 2) and not self.two_small):
                    self.printAllPathsUtil(i, d, visited, path)
                     
        # Remove current vertex from path[] and mark it as unvisited
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
  
  
    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):
 
        # Mark all the vertices as not visited
        visited = {}
 
        # Create an array to store paths
        path = []
 
        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)

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
g.printAllPaths("start","end")
g.getNumOfPaths()
