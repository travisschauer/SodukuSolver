# Travis Schauer
# 12/4/2021
# Implements SudokuConnections class

'''
Created using a guide by Ishaan Gupta
https://medium.com/code-science/sudoku-solver-graph-coloring-8f1b4df47072
'''

from graph import Graph

class SudokuConnections:
    # Constructor
    def __init__(self):
        self.graph = Graph()

        self.rows = 9
        self.cols = 9
        self.total_blocks = self.rows * self.cols

        self.__generateGraph()
        self.connectEdges()

        self.allIds = self.graph.getAllNodesIds()

    # Methods
    def __generateGraph(self):
        for idx in range(1, self.total_blocks + 1):
            _ = self.graph.addNode(idx)

    def connectEdges(self):
        # Connects nodes according to rules
        matrix = self.__getGridMatrix()

        head_connections = dict()

        for row in range(9):
            for col in range(9):
                head = matrix[row][col]
                connections = self.__whatToConnect(matrix, row, col)

                head_connections[head] = connections

        self.__connectThose(head_connections=head_connections)

    def __connectThose(self, head_connections):
        for head in head_connections.keys():
            connections = head_connections[head]
            for key in connections:
                for v in connections[key]:
                    self.graph.addEdge(src=head, dst=v)

    def __whatToConnect(self, matrix, rows, cols):
        connections = dict()

        row = []
        col = []
        block = []

        # Rows
        for c in range(cols + 1, 9):
            row.append(matrix[rows][c])

        connections["rows"] = row

        # Columns
        for r in range(rows + 1, 9):
            col.append(matrix[r][cols])

        connections["cols"] = col

        # Blocks
        if rows % 3 == 0:

            if cols % 3 == 0:

                block.append(matrix[rows + 1][cols + 1])
                block.append(matrix[rows + 1][cols + 2])
                block.append(matrix[rows + 2][cols + 1])
                block.append(matrix[rows + 2][cols + 2])

            elif cols % 3 == 1:

                block.append(matrix[rows + 1][cols - 1])
                block.append(matrix[rows + 1][cols + 1])
                block.append(matrix[rows + 2][cols - 1])
                block.append(matrix[rows + 2][cols + 1])

            elif cols % 3 == 2:

                block.append(matrix[rows + 1][cols - 2])
                block.append(matrix[rows + 1][cols - 1])
                block.append(matrix[rows + 2][cols - 2])
                block.append(matrix[rows + 2][cols - 1])

        elif rows % 3 == 1:

            if cols % 3 == 0:

                block.append(matrix[rows - 1][cols + 1])
                block.append(matrix[rows - 1][cols + 2])
                block.append(matrix[rows + 1][cols + 1])
                block.append(matrix[rows + 1][cols + 2])

            elif cols % 3 == 1:

                block.append(matrix[rows - 1][cols - 1])
                block.append(matrix[rows - 1][cols + 1])
                block.append(matrix[rows + 1][cols - 1])
                block.append(matrix[rows + 1][cols + 1])

            elif cols % 3 == 2:

                block.append(matrix[rows - 1][cols - 2])
                block.append(matrix[rows - 1][cols - 1])
                block.append(matrix[rows + 1][cols - 2])
                block.append(matrix[rows + 1][cols - 1])

        elif rows % 3 == 2:

            if cols % 3 == 0:

                block.append(matrix[rows - 2][cols + 1])
                block.append(matrix[rows - 2][cols + 2])
                block.append(matrix[rows - 1][cols + 1])
                block.append(matrix[rows - 1][cols + 2])

            elif cols % 3 == 1:

                block.append(matrix[rows - 2][cols - 1])
                block.append(matrix[rows - 2][cols + 1])
                block.append(matrix[rows - 1][cols - 1])
                block.append(matrix[rows - 1][cols + 1])

            elif cols % 3 == 2:

                block.append(matrix[rows - 2][cols - 2])
                block.append(matrix[rows - 2][cols - 1])
                block.append(matrix[rows - 1][cols - 2])
                block.append(matrix[rows - 1][cols - 1])

        connections["blocks"] = block
        return connections

    def __getGridMatrix(self):
        matrix = [[0 for cols in range(self.cols)]
                  for rows in range(self.rows)]

        count = 1
        for rows in range(9):
            for cols in range(9):
                matrix[rows][cols] = count
                count += 1
        return matrix