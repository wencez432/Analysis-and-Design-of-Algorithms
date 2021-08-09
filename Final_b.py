import numpy
import matplotlib.pyplot as plt

class Node:
    def __init__(self, container, mat):
        self.container = container
        self.mat = mat

    @staticmethod
    def get_cost(node, i):
        cost = node.mat[i][node.container]
        return cost

    @staticmethod
    def get_total_cost(solutions):
        cost = 0
        for i in range(len(solutions)):
            cost += Node.get_cost(solutions[i], i)
        return cost


if __name__ == '__main__':
    matiz = [[30, 40, 70],
            [60, 20, 10],
            [40, 90, 30]]
    cont = [0,1,2]
    solution = []
    for i in range(3):
        c = numpy.random.choice(cont)
        cont.remove(c)
        solution.append(Node(c, matiz))

    # Simulated annealing algorithm
    cost0 = Node.get_total_cost(solution)
    T = 30.0 # Temperatura inicial
    factor = 0.99 # factor de decrecimiento

    for i in range(1000):
        for j in range(200):
            # Generando una nueva solución
            c1, c2 = numpy.random.randint(0, len(solution), size=2)

            temp = solution[c1]
            solution[c1] = solution[c2]
            solution[c2] = temp

            # Calculando el nuevo costo
            cost1 = Node.get_total_cost(solution)

            if cost1 < cost0:
                cost0 = cost1
            else:
                r = numpy.random.uniform()
                p = numpy.exp((cost0-cost1)/T)
                if r < p:
                    cost0 = cost1
                else:
                    temp = solution[c1]
                    solution[c1] = solution[c2]
                    solution[c2] = temp
        T = T*factor

    for i in range(len(solution)):
        print("Ciudad " + str(i+1) + " contenedor " + str(solution[i].container + 1))
    print("Menor costo: " + str(Node.get_total_cost(solution)) + " minutos.")
