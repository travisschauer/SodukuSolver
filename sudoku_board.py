# Travis Schauer
# 12/4/2021
# Implements SudokuBoard class

'''
Created using a guide by Ishaan Gupta
https://medium.com/code-science/sudoku-solver-graph-coloring-8f1b4df47072
'''

from sudoku_connections import SudokuConnections

class SudokuBoard:
    # Constructor
    def __init__(self):
        self.board = self.getBoard()

        self.sudokuGraph = SudokuConnections()
        self.mappedGrid = self.__getMappedMatrix()

    # Methods
    def __getMappedMatrix(self):
        matrix = [[0 for cols in range(9)]
        for rows in range(9)]

        count = 1
        for rows in range(9):
            for cols in range(9):
                matrix[rows][cols] = count
                count+=1
        return matrix

    def getBoard(self):

        board = [
            [4,0,0,0,0,0,9,0,0],
            [0,0,0,0,3,0,0,0,0],
            [0,1,0,0,6,5,0,4,0],
            [0,0,0,3,0,0,0,5,0],
            [0,0,6,0,5,2,7,0,0],
            [0,2,0,9,0,0,0,0,0],
            [0,0,0,2,0,0,0,0,0],
            [0,6,0,0,4,1,0,9,0],
            [0,0,7,0,0,0,0,0,8]
        ]
        return board

    def printBoard(self):

        print("    1 2 3     4 5 6     7 8 9")
        for i in range(len(self.board)):
            if i%3 == 0:
                print("  - - - - - - - - - - - - - - ")

            for j in range(len(self.board[i])):
                if j %3 == 0:
                    print(" |  ", end = "")
                if j == 8:
                    print(self.board[i][j]," | ", i+1)
                else:
                    print(f"{ self.board[i][j] } ", end="")
        print("  - - - - - - - - - - - - - - ")

    def is_Blank(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    def graphColoringInitializeColor(self):
        # Fills the colors given from the board
        color = [0] * (self.sudokuGraph.graph.totalV+1)
        given = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0:
                    idx = self.mappedGrid[row][col]
                    color[idx] = self.board[row][col]
                    given.append(idx)
        return color, given

    def solveGraphColoring(self, m=9):
        # Fills the rest of colors
        color, given = self.graphColoringInitializeColor()
        if self.__graphColorUtility(m =m, color=color, v =1, given=given) is None:
            print(":(")
            return False
        count = 1
        for row in range(9):
            for col in range(9):
                self.board[row][col] = color[count]
                count += 1
        return color

    def __graphColorUtility(self, m, color, v, given):
        if v == self.sudokuGraph.graph.totalV+1:
            return True
        for c in range(1, m+1):
            if self.__isSafe2Color(v, color, c, given) == True:
                color[v] = c
                if self.__graphColorUtility(m, color, v+1, given):
                    return True
            if v not in given:
                color[v] = 0

    def __isSafe2Color(self, v, color, c, given):
        if v in given and color[v] == c:
            return True
        elif v in given:
            return False

        for i in range(1, self.sudokuGraph.graph.totalV+1):
            if color[i] == c and self.sudokuGraph.graph.isNeighbour(v, i):
                return False
        return True
