import numpy as np
import time

def SSM(Q,izq,der):
    centro = int((izq + der)/2)
    if izq == der:
        if Q[izq] < 0:
            return 0,-1,-1
        else:
            return Q[izq],izq,der
    else:
        m1,p,q = SSM(Q, izq, centro)
        m2,r,s = SSM(Q, centro + 1, der)
        sp = 0
        max_izq = 0
        x_izq = -1
        if p >= 0:
            for i in range(centro,p-1,-1):
                sp += Q[i]
                if sp > max_izq:
                    max_izq = sp
                    x_izq = i
        sp = 0
        max_der = 0
        x_der = -1
        for i in range(centro + 1,s+1):
            sp += Q[i]
            if sp > max_der:
                max_der = sp
                x_der = i
        ssm = max(m1, m2, max_izq + max_der)
        if m1 == ssm:
            return m1,p,q
        elif m2 == ssm:
            return m2,r,s
        else:
            return max_izq + max_der,x_izq,x_der

def SSM_BruteForce(Q):
    n = len(Q)
    smax = 0
    for i in range(n):
        s = 0
        for j in range(i,n):
            s += Q[j]
            if s > smax:
                smax = s
                ip = i
                jp = j
    return smax,ip,jp

def SSM_Lineal(Q):
    n = len(Q)
    ssm = 0
    sp = 0
    io = 0
    for j in range(n):
        sp += Q[j]
        if sp > ssm:
            ssm = sp
            ip = io + 1
            jp = j
        elif sp < 0:
            sp = 0
            io = j
    return ssm,ip,jp

n = 10000
Q = np.random.randint(-100, 100, size = n)
print("Subsecuencia de suma maxima\n",Q)
print("Para n = ",n)
print("Formato de respuesta (suma maxima, inicio, fin)")
print("\n")

start = time.time()
print("SSM lineal O(n): ",SSM_Lineal(Q))
finish = time.time()
print("Tiempo: ",finish - start)

print("\n------------------------------------------\n")

start = time.time()
print("Divide y venceras O(nlogn): ",SSM(Q, 0, n-1))
finish = time.time()
print("Tiempo: ",finish - start)

print("\n------------------------------------------\n")

start = time.time()
print("Fuerza bruta mejorado O(n^2): ",SSM_BruteForce(Q))
finish = time.time()
print("Tiempo: ",finish - start)