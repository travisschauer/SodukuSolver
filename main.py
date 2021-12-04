# Travis Schauer
# 12/4/2021
# This program compiles a sodoku board and solves it
# using the idea of graph colorings

'''
Created using a guide by Ishaan Gupta
https://medium.com/code-science/sudoku-solver-graph-coloring-8f1b4df47072
'''

from sudoku_board import SudokuBoard

def main():
    s = SudokuBoard()
    print("Board:")
    s.printBoard()
    print("\n...")
    s.solveGraphColoring(m=9)
    print("\nSolution:")
    s.printBoard()

if __name__ == "__main__":
    main()