# Travis Schauer
# 12/4/2021
# Implements graph class

'''
Created using a guide by Ishaan Gupta
https://medium.com/code-science/sudoku-solver-graph-coloring-8f1b4df47072
'''

from node import Node

class Graph:
    # Total number of vertices
    totalV = 0

    # Constructor
    def __init__(self):
        self.allNodes = dict()

    # Methods
    def addNode(self, idx):
        if idx in self.allNodes:
            return None

        Graph.totalV += 1
        node = Node(idx=idx)
        self.allNodes[idx] = node
        return node

    def addNodeData(self, idx, data):
        # Adds node to idx
        if idx in self.allNodes:
            node = self.allNodes[idx]
            node.setData(data)
        else:
            print("No ID to add the data.")

    def addEdge(self, src, dst, wt=0):
        # Adds edge between 2 nodes
        self.allNodes[src].addNeighbour(self.allNodes[dst], wt)
        self.allNodes[dst].addNeighbour(self.allNodes[src], wt)

    def isNeighbour(self, u, v):
        # Checks existence of a neighbor
        if u >= 1 and u <= 81 and v >= 1 and v <= 81 and u != v:
            if v in self.allNodes[u].getConnections():
                return True
        return False

    def printEdges(self):
        for idx in self.allNodes:
            node = self.allNodes[idx]
            for con in node.getConnections():
                print(node.getID(), " --> ",
                      self.allNodes[con].getID())

    def DFS(self, start):
        # Works a stack
        visited = [False] * Graph.totalV

        if start in self.allNodes.keys():
            self.__DFSUtility(node_id=start, visited=visited)
        else:
            print("Start Node not found")

    def __DFSUtility(self, node_id, visited):
        # Checks if nodes have been visited
        visited = self.__setVisitedTrue(visited=visited, node_id=node_id)

        print(self.allNodes[node_id].getID(), end=" ")

        for i in self.allNodes[node_id].getConnections():
            if visited[self.allNodes[i].getID()] == False:
                self.__DFSUtility(node_id=self.allNodes[i].getID(),
                                  visited=visited)

    def BFS(self, start):
        # Works a queue
        visited = [False] * Graph.totalV

        if start in self.allNodes.keys():
            self.__BFSUtility(node_id=start, visited=visited)
        else:
            print("Start Node not found")

    def __BFSUtility(self, node_id, visited):
        queue = []
        visited = self.__setVisitedTrue(visited=visited, node_id=node_id)

        queue.append(node_id)

        while queue != []:
            x = queue.pop(0)
            print(self.allNodes[x].getID(), end=" ")

            for i in self.allNodes[x].getConnections():
                idx = self.allNodes[i].getID()
                if visited[idx] == False:
                    queue.append(idx)
                    visited = self.__setVisitedTrue(visited=visited,
                                                    node_id=idx)

    def __setVisitedTrue(self, visited, node_id):
        visited[node_id] = True
        return visited

    # getter
    def getNode(self, idx):
        if idx in self.allNodes:
            return self.allNodes[idx]
        return None

    def getAllNodesIds(self):
        return self.allNodes.keys()