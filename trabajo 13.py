class Grafo:
    def __init__(self):
        self.grafo = {}
    
    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = {}
 
    def agregar_arista(self, origen, destino, peso):

        if origen not in self.grafo[destino]:
            self.grafo[destino][origen] = {}
        if destino not in self.grafo[origen]:
            self.grafo[origen][destino] = {}

        self.grafo[origen][destino] = peso
        self.grafo[destino][origen] = peso

    def bfs(self, inicio, final, parent):
        visitados = {inicio}
        cola = [inicio]
        
        while cola:
            nodo_actual = cola.pop(0)
            
            for vecino, capacidad in self.grafo[nodo_actual].items():
                if vecino not in visitados and capacidad > 0:
                    visitados.add(vecino)
                    parent[vecino] = nodo_actual
                    if vecino == final:
                        return True
                    cola.append(vecino)
        return False
    
    def edmonds_karp(self, inicio, final):
        max_flow = 0
        parent = {}
        
        while self.bfs(inicio, final, parent):
            path_flow = float('Inf')
            s = final
            
            while s != inicio:
                path_flow = min(path_flow, self.grafo[parent[s]][s])
                s = parent[s]
            
            max_flow += path_flow
            v = final
            
            while v != inicio:
                u = parent[v]
                self.grafo[u][v] -= path_flow
                self.grafo[v][u] += path_flow
                v = parent[v]
        
        return max_flow


c = int(input())

for i in range(c):
        m, n = map(int, input().split())
        nm = m//6
        remeras = {'XXL':0, 'XL':1, 'L':2, 'M':3, 'S':4, 'XS':5}

        g = Grafo()
        #agregamos el nodo de inicio y el nodo de fin
        g.agregar_nodo(n+7)
        g.agregar_nodo(n+8)
        #agregamos los nodos de las remeras y los conectamos con el nodo de inicio
        for j in range(6):
             g.agregar_nodo(j)
             g.agregar_arista(j, n+7, nm)
        #agregamos los nodos de los voluntarios y los conectamos con los nodos de las remeras y con el nodo de fin
        for j in range(6, n+6):
            g.agregar_nodo(j)
            a, b = map(str, input().split())
            g.agregar_arista(j, remeras[a], 1)
            g.agregar_arista(j, remeras[b], 1)
            g.agregar_arista(j, n+8, 1)

        max_flow = g.edmonds_karp(n+7, n+8)

        if max_flow == n:
            print("YES")

        else:
            print("NO")