import numpy
import matplotlib.pyplot as plt

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def get_distance(a, b):
        return numpy.sqrt(numpy.abs(a.x-b.x)+numpy.abs(a.y-b.y))

    @staticmethod
    def get_total_distance(coords):
        dist = 0
        for first, second in zip(coords[:-1], coords[1:]):
            dist += Coordinate.get_distance(first, second)
        dist += Coordinate.get_distance(coords[0], coords[-1])
        return dist

if __name__ == '__main__':
    # Crearemos las coordenadas
    coords = []
    for i in range(10):
        coords.append(Coordinate(numpy.random.uniform(), numpy.random.uniform()))

    # graficos
    fig = plt.figure(figsize=(10, 10))
    gs = fig.add_gridspec(2,2)
    ax1 = fig.add_subplot(gs[0,0])
    ax2 = fig.add_subplot(gs[0,1])
    ax3 = fig.add_subplot(gs[1,0])
    ax4 = fig.add_subplot(gs[1,1])
    costx = []
    costy = []
    tempx = []
    tempy = []
    probx = []
    proby = []

    # Simulated annealing algorithm
    cost0 = Coordinate.get_total_distance(coords)
    T = 30.0 # Temperatura inicial
    factor = 0.99 # factor de decrecimiento

    for i in range(1000):
        # graficando
        costx.append(i)
        costy.append(cost0)
        tempx.append(i)
        tempy.append(T)
        # actualizando grafico solucion
        ax1.cla()
        ax1.set_title('Ruta {}'.format(i+1))
        for first, second in zip(coords[:-1], coords[1:]):
            ax1.plot([first.x, second.x], [first.y, second.y], 'b')
        ax1.plot([coords[0].x, coords[-1].x], [coords[0].y, coords[-1].y], 'b')
        for c in coords:
            ax1.plot(c.x, c.y, 'ro')
        ax1.axis([0, 1, 0, 1])
        # actualizando grafico del costo
        ax2.cla()
        ax2.plot(costx, costy)
        ax2.set_title('Distancia total (costo)')
        ax2.set_xlabel('iteracion')
        ax2.set_ylabel('Distancia')
        ax2.text(400,16,r'Costo = {:4f}'.format(cost0))
        ax2.axis([0, 1000, 0, 18])
        # actualizando grafico de la temperatura
        ax4.cla()
        ax4.plot(tempx, tempy)
        ax4.set_title('Temperatura')
        ax4.set_xlabel('iteracion')
        ax4.set_ylabel('Temperatura')
        ax4.text(400,25,r'Temperatura = {:4f}'.format(T))
        ax4.axis([0, 1000, 0, 30])
        p = 1
        t_p = 1

        for j in range(200):
            # Generando una nueva solución
            c1, c2 = numpy.random.randint(0, len(coords), size=2)

            temp = coords[c1]
            coords[c1] = coords[c2]
            coords[c2] = temp

            # Calculando el nuevo costo
            cost1 = Coordinate.get_total_distance(coords)

            if cost1 < cost0:
                cost0 = cost1
            else:
                r = numpy.random.uniform()
                p = numpy.exp((cost0-cost1)/T)
                if r < p:
                    cost0 = cost1
                    t_p = p
                else:
                    temp = coords[c1]
                    coords[c1] = coords[c2]
                    coords[c2] = temp
        T = T*factor

        probx.append(i)
        proby.append(t_p)
        # actualizando grafico de probabilidad de aceptacion
        ax3.cla()
        ax3.plot(probx, proby,ls = ' ', marker ='.', alpha = 0.3)
        ax3.set_title('Probabilidad de aceptación')
        ax3.set_xlabel('iteracion')
        ax3.set_ylabel('Probabilidad de aceptación')
        ax3.axis([0, 1000, 0, 1])
        plt.draw()
        plt.pause(0.03)

    plt.show()
