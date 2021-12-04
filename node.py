# Travis Schauer
# 12/4/2021
# Implements a class for nodes

'''
Created using a guide by Ishaan Gupta
https://medium.com/code-science/sudoku-solver-graph-coloring-8f1b4df47072
'''

class Node:
    # Constructor
    def __init__(self, idx, data = 0):
        self.id = idx
        self.data = data
        self.connectedTo = dict()

    # Methods
    def addNeighbour(self, neighbour, weight = 0):
        # Adds neighbour, with weight, to dictionary
        if neighbour.id not in self.connectedTo.keys():
            self.connectedTo[neighbour.id] = weight

    def __str__(self):
        return str(self.data) + " Connected to : " + \
            str([x.data for x in self.connectedTo])

    # setters/getters
    def setData(self, data):
        self.data = data

    def getConnections(self):
        return self.connectedTo.keys()

    def getID(self):
        return  self.id

    def getData(self):
        return self.data

    def getWeight(self, neighbour):
        return self.connectedTo[neighbour.id]
