import copy
from heapq import heappush, heappop

# 8 puzzle(n=3)
# 15 puzzle(n=4)
# 24 puzzle(n=5)...
global n

# movimientos
# abajo, izquierda, arriba, derecha
row = [ 1, 0, -1, 0 ]
col = [ 0, -1, 0, 1 ]

# Clase para la lista de prioridades
class priorityQueue:

    def __init__(self):
        self.heap = []

    # Inserta nuevo elemento a la lista
    def push(self, k):
        heappush(self.heap, k)

    # Método que remueve el menor elemento de la lista de prioridades
    def pop(self):
        return heappop(self.heap)

    def empty(self):
        if not self.heap:
            return True
        else:
            return False

# Estructura del nodo
class node:

    def __init__(self, parent, mat, empty_tile_pos, cost, level):
        self.parent = parent
        self.mat = mat
        self.empty_tile_pos = empty_tile_pos
        self.cost = cost
        self.level = level

    def __lt__(self, nxt):
        return (self.cost + self.level) < (nxt.cost + nxt.level)
        #return self.cost < nxt.cost

def calculateCost(mat, final) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            # Si el casillero no vació del estado actual esta fuera de lugar respecto al estado final
            if ((mat[i][j]) and (mat[i][j] != final[i][j])):
                count += 1
    return count

def newNode(mat, empty_tile_pos, new_empty_tile_pos, level, parent, final) -> node:
    # Copiamos el estado del tablero actual
    new_mat = copy.deepcopy(mat)

    # Movemos la ficha una posición
    x1 = empty_tile_pos[0]
    y1 = empty_tile_pos[1]
    x2 = new_empty_tile_pos[0]
    y2 = new_empty_tile_pos[1]
    # intercambio de fichas
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]

    # Calculamos el numero de casillas fuera de lugar
    cost = calculateCost(new_mat, final)

    new_node = node(parent, new_mat, new_empty_tile_pos, cost, level)
    return new_node

# Función que imprime el tablero
def printMatrix(mat):
    for i in range(n):
        for j in range(n):
            print(f"{mat[i][j]:>2}", end=" ")
        print()

# Función que revisa si la coordenada (x,y) esta dentro del tablero
def isSafe(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

# Imprime camino desde nodo raíz a nodo destino
def printPath(root):
    if root == None:
        return

    printPath(root.parent)
    print("Costo h(X): ",root.cost)
    printMatrix(root.mat)
    print()

def solve(initial, empty_tile_pos, final):
    pq = priorityQueue()

    # Creamos nodo raíz
    MaxCost = calculateCost(initial, final)
    root = node(None, initial, empty_tile_pos, MaxCost, 0)
    pq.push(root)

    while not pq.empty():
        """
        print("Lista de nodos vivos:\n")
        for e in pq.heap:
            print("Costo h(X): ",e.cost)
            printMatrix(e.mat)
        """

        minimum = pq.pop()

        print("Costo total del nodo elejido: ",minimum.cost + minimum.level)
        # Si estamos en nodo solución
        if minimum.cost == 0:
            print("\nSolucion")
            print("---------")
            printPath(minimum)
            return

        # Generamos todos los hijos posibles
        for i in range(4):
            new_tile_pos = [
                minimum.empty_tile_pos[0] + row[i],
                minimum.empty_tile_pos[1] + col[i], ]

            if isSafe(new_tile_pos[0], new_tile_pos[1]):
                # Creamos un nodo hijo
                child = newNode(minimum.mat, minimum.empty_tile_pos, new_tile_pos, minimum.level + 1, minimum, final,)
                # Añadimos el hijo a la lista de nodos vivos
                if child.cost <= MaxCost:
                    pq.push(child)

print("Ejemplo 1")
print("-----------------------------------\n")
n = 3
initial = [
    [ 1, 2, 3 ],
    [ 5, 6, 0 ],
    [ 7, 8, 4 ] ]

final = [
    [ 1, 2, 3 ],
    [ 5, 8, 6 ],
    [ 0, 7, 4 ] ]

empty_tile_pos = [ 1, 2 ]

solve(initial, empty_tile_pos, final)


print("Ejemplo 2")
print("-----------------------------------\n")
n = 4
initial = [
    [ 5, 1, 4, 8 ],
    [ 3,10, 2, 6 ],
    [ 9, 0, 7,12 ],
    [13,14,11,15 ] ]

final = [
    [ 1, 2, 3, 4 ],
    [ 5, 6, 7, 8 ],
    [ 9,10,11,12 ],
    [13,14,15, 0 ] ]

empty_tile_pos = [ 2, 1 ]

solve(initial, empty_tile_pos, final)

