import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}
    
    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def agregar_arista(self, origen, destino, peso):
        self.grafo[origen].append((destino, peso))
        self.grafo[destino].append((origen, peso))
    
    def semidijkstra(self, inicio, final):
        distancias = {nodo: float('infinity') for nodo in self.grafo}
        distancias[inicio] = 0
        visitados = []
        heapq.heappush(visitados, (0, inicio))
        
        while visitados:
            tiempo, nodo_actual = heapq.heappop(visitados)

            for vecino, peso in self.grafo[nodo_actual]:
                distancia = tiempo + peso
                if distancias[vecino] > distancia:
                    distancias[vecino] = distancia
                    heapq.heappush(visitados, (distancia, vecino))
        
        return distancias
def main():
    try:

        n, k = map(int, input().split())
        while n!= 0:
            velocity = list(map(int, input().split()))
    
            ascensores = []
            for _ in range(n):
                ascensores.append(list(map(int, input().split())))
        
            pisos = []
            for i in range(n):
                for j in range(len(ascensores[i])):
                    if ascensores[i][j] not in pisos:
                        pisos.append(ascensores[i][j])
    
            grafo = Grafo()

            #agrego un nodo correspondiente a cada piso, para que se puedan conectar los nodos de los ascensores entre si
            for j in range(len(pisos)):
                grafo.agregar_nodo(pisos[j]+ 100*(n+1))
    
            #agrego los nodos y las aristas de los ascensores y los pisos en los que frenan
            for i in range(n):
                for j in range(1,len(ascensores[i])):
                    if j == 1:
                        grafo.agregar_nodo(ascensores[i][j-1] +100*i)
                        grafo.agregar_arista((ascensores[i][j-1] + 100*(n+1)), (ascensores[i][j-1] + 100*i), 30)
                    grafo.agregar_nodo((ascensores[i][j] +100*i))
                    #les pongo de peso 30, ya que como se conectan dos ascensores al nodo del piso => 2*30 = 60 que es el peso que queriamos
                    grafo.agregar_arista((ascensores[i][j] +100*i),(ascensores[i][j] + 100*(n+1)),30)
                    grafo.agregar_arista((ascensores[i][j-1] + 100*i), (ascensores[i][j] + 100*i), velocity[i] * abs(ascensores[i][j] - ascensores[i][j-1]))


            distancias = grafo.semidijkstra(100*(n+1), (k + 100*(n+1)))

            if (k+ (n+1)*100) not in distancias or distancias[(k+ (n+1)*100)] == float('infinity'):
                print("IMPOSSIBLE")
                #respuestas.append('IMPOSSIBLE')
            else:
                if distancias[(k+ (n+1)*100)] == 0:
                    print(0)
                    #respuestas.append(0)
                else:
                    #le restamos 60 porque el peso de la primera conexion del piso con el ascensor y la última no las contamos
                    print(distancias[(k+ (n+1)*100)] - 60)
                    #respuestas.append(distancias[(k,n+1)] - 60)

            n, k = map(int, input().split())
    except EOFError:
        pass
    

            
if __name__ == "__main__":
    main()