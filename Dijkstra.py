import math
import numpy as np

def dijkstra(S,W,D,i,f,n):
    if i not in S:
        S.append(i)
        for j in range(n):
            D[i][j] = W[i][j]
        for k in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + W[k][j])
    return S,D,D[i][f]

n = 10
#Crear grafo aleatorio con n nodos

#Generar matriz de adyacencia
M = np.random.randint(0,2,(n,n))
#Asignar pesos
W = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        if(M[i][j] == 1):
            if i == j:
                W[i][j] = 0
            else:
                W[i][j] = np.random.randint(1,11)
        else:
            W[i][j] = math.inf
#Creamos matriz de distancias
D = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        D[i][j] = math.inf

#Creamos matriz S
S = []

print("Matriz de adyacencia\n",M)
print("Pesos de las aristas\n",W)

s = 0
f = 0
while s != -1 and f != -1:
    s = int(input("Ingrese nodo inicial: "))
    f = int(input("Ingrese nodo final: "))
    if s != -1 and f != -1:
        S,D,min_dist = dijkstra(S,W,D,s,f,n)
        print("Distancia minima es: ",min_dist)
        print("\nMatriz de distancias\n",D)