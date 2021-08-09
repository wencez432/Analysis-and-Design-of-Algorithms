import random

def LocalSearch(e,w,c,W):
    sol = [0,0,0,0,0]
    sol_c = 0
    sol_w = 0
    sol_p = [0,0,0,0,0]
    # Generando solucion inicial de forma aleatoria
    for i in range(len(e)):
        sol_p[i] = random.randint(0,1)
    MAX_ITER = 300
    count = 0
    while count < MAX_ITER:
        sum_w = int(0)
        sum_c = int(0)
        # Calculando el peso y beneficio de una nueva posible soluciom
        for j in range(len(e)):
            if sol_p[j] == 1:
                sum_w += w[j]
                sum_c += c[j]
        # si la posible solucion tiene peso menor al maximo
        if sum_w <= W:
            # Actualizamos la solucion
            if sol_c < sum_c:
                for i in range(len(sol)):
                    sol[i] = sol_p[i]
                sol_c = sum_c
                sol_w = sum_w
        # Generando vecinos
        # Cambiando un elemento de forma aleatoria
        op = random.randint(0,len(e)-1)
        if sol_p[op] == 1:
            sol_p[op] = 0
        else:
            sol_p[op] = 1
        count += 1
    return sol, sol_c, sol_w

def knapSack(W, wt, val, n):
    if n == 0 or W == 0 :
        return 0

    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)

    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),knapSack(W, wt, val, n-1))

e = [1, 2, 3, 4, 5]
w = [5, 7, 6, 2, 1]
c = [4, 9, 5, 1, 2]
W = 20

sol , cost, weight = LocalSearch(e,w,c,W)

print("Solucion: {}, Beneficio: {}, Peso solucion: {}".format(sol, cost, weight))

val = [4, 9, 5, 1, 2]
wt = [5, 7, 6, 2, 1]
W = 20
n = len(val)
print("Beneficio: {}".format(knapSack(W, wt, val, n)))