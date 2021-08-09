import math
import numpy as np

def printMatrix(M, n):
    for i in range(n):
        for j in range(n):
            print("{:^7}".format(M[i][j]), end="")
        print()

def push_relabel(C, source: int, sink: int) -> int:
    n = len(C)  # C matriz de capacidades
    F = [[0] * n for _ in range(n)]
    # la capacidad residual de u a v es C[u][v] - F[u][v]

    height = [0] * n  # haltura o distancia de un nodo (etiquetas)
    excess = [0] * n  # exceso (flujo hacia el nodo - el flujo desde el nodo)
    seen   = [0] * n  # vecinos vistos desde el ultimo reetiquetado
    # node "queue"
    nodelist = [i for i in range(n) if i != source and i != sink]

    def push(u, v):
        send = min(excess[u], C[u][v] - F[u][v])
        F[u][v] += send
        F[v][u] -= send
        excess[u] -= send
        excess[v] += send

    def relabel(u):
        # En cuentra la menor distancia o haltura (etiqueta) para poder realiar un push,
        # si en caso se pueda realizar.
        min_height = math.inf
        for v in range(n):
            if C[u][v] - F[u][v] > 0:
                min_height = min(min_height, height[v])
                height[u] = min_height + 1

    def discharge(u):
        while excess[u] > 0:
            if seen[u] < n:  # revisa el siguiente vecino
                v = seen[u]
                if C[u][v] - F[u][v] > 0 and height[u] > height[v]:
                    push(u, v)
                else:
                    seen[u] += 1
            else:  # Se revisaron todos los vecinos. (realizamos un reetiquetado)
                relabel(u)
                seen[u] = 0

    height[source] = n  # el camino mas largo desde la fuente hacia el sumidero tiene longitud menor que n
    excess[source] = math.inf  # enviar el maximo flujo posible desde la fuente hacia sus vecinos
    for v in range(n):
        push(source, v)

    p = 0
    while p < len(nodelist):
        u = nodelist[p]
        old_height = height[u]
        discharge(u)
        if height[u] > old_height:
            nodelist.insert(0, nodelist.pop(p))  # mover al inicio de la lista
            p = 0  # empieza desde el inicio de la lista
        else:
            p += 1

    print("Matriz de flujos")
    printMatrix(F, len(F))
    return sum(F[source])

if __name__ == "__main__":

    n = 6
    capacities = np.zeros((n,n))
    capacities[0][1] = 15
    capacities[0][2] = 4
    capacities[1][3] = 12
    capacities[2][4] = 10
    capacities[3][2] = 3
    capacities[3][5] = 7
    capacities[4][1] = 5
    capacities[4][5] = 10

    print("Matriz de capacidades")
    printMatrix(capacities, n)
    print("Max flow: ", push_relabel(capacities,0,n-1))