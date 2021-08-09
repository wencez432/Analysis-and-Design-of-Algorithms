import numpy as np

global N

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(int(board[i][j]), end = " ")
        print()

def isSafe(board, row, col):
    # Revisamos la fila al lado izquierdo
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Revisamos las diagonales
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solveNQUtil(board, col):
    # Caso base si ya se colocaron todas las reinas
    if col >= N:
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            print("\nColocando reina en la columna "+str(col))
            printSolution(board)
            if solveNQUtil(board, col + 1) == True:
                return True
            # Realizamos el backtracking
            board[i][col] = 0
            print("\nBacktracking")
            printSolution(board)
    return False

N = int(input("Ingrese valor de N: "))
board = np.zeros((N,N))

if solveNQUtil(board, 0) == False:
    print ("No existe solucion")
print("\nSolucion encontrada")
printSolution(board)
