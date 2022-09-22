from typing import List

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited =[]
        queue = []
        
        return None


    def bfs(visited, graph, node, queue):
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0) 
            print (s, end = " ") 

            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)