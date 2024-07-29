class Grafo:
    def __init__(self):
        self.grafo = {}
    
    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = {}
 
    def agregar_arista(self, origen, destino, peso):
        if destino not in self.grafo[origen]:
            self.grafo[origen][destino] = 0
        self.grafo[origen][destino] += peso
        if origen not in self.grafo[destino]:
            self.grafo[destino][origen] = 0

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
    
    # def edmonds_karp(self, inicio, final):
    #     max_flow = 0
    #     parent = {}
        
    #     while self.bfs(inicio, final, parent):
    #         path_flow = float('Inf')
    #         s = final
            
    #         while s != inicio:
    #             path_flow = min(path_flow, self.grafo[parent[s]][s])
    #             s = parent[s]
            
    #         max_flow += path_flow
    #         v = final
            
    #         while v != inicio:
    #             u = parent[v]
    #             self.grafo[u][v] -= path_flow
    #             self.grafo[v][u] += path_flow
    #             v = parent[v]
        
    #     return max_flow

    def edmonds_karp(self, inicio, final):
        max_flow = 0
        parent = {}
    
        while self.bfs(inicio, final, parent):
            path_flow = float('Inf')
            s = final
            path = []
        
            while s != inicio:
                path_flow = min(path_flow, self.grafo[parent[s]][s])
                path.append(s)
                s = parent[s]
            path.append(inicio)
            path.reverse()
        
            print(f"Path found: {path}, flow: {path_flow}")  # Debug output
        
            max_flow += path_flow
            v = final
        
            while v != inicio:
                u = parent[v]
                self.grafo[u][v] -= path_flow
                self.grafo[v][u] += path_flow
                v = parent[v]
    
        return max_flow
    
def main():
    try:
        x,y,p = map(int, input().split())
        results = []
        b = 'b'
        while x != 0:

            n = x*y
            # cada simbolo tiene una capacidad de entrada y otra de salida
            symbols = {'*':(0,1),'~':(0,0),'#':(n,n),'@':(n,n),'.':(1,1)}
        
            g = Grafo()
            #creamos los nodos de inicio y fin
            g.agregar_nodo((0,n+1))
            g.agregar_nodo((n+1,n+1))

            mapa = []
            for i in range(x):
                line = input()
                mapa.append(line)
                for j in range(len(line)):
                    g.agregar_nodo((i,j))
                    #conectamos las personas con el nodo de inicio, con capacidad/peso = 1
                    if line[j] == '*':
                        g.agregar_arista((0,n+1), (i,j), 1)

                    #conectamos los troncos con el nodo final con capacidad/peso = p
                    if line[j] == '#':
                        g.agregar_arista((i,j), (n+1,n+1), p)

                    #creamos un nodo fantasma para cada hielo del mapa y conectamos el flujo saliente entre ellos
                    if line[j] == '.':
                        g.agregar_nodo(((i,j),b))
                        g.agregar_arista((i,j), ((i,j),b), 1)


            #conectamos el mapa entre si
            #primero conectamos todo el centro del mapa
            for i in range(1,x-1):
                for j in range(1,y-1):
                    #si el punto del mapa es un hielo, el flujo sale desde su nodo fantasma
                    if mapa[i][j]== '.':
                        g.agregar_arista(((i,j),b),(i,j-1),1)
                        g.agregar_arista(((i,j),b),(i,j+1),1)
                        g.agregar_arista(((i,j),b),(i+1,j),1)
                        g.agregar_arista(((i,j),b),(i-1,j),1)
                    else:
                        g.agregar_arista((i,j),(i,j+1),min(symbols[mapa[i][j]][1], symbols[mapa[i][j+1]][0]))
                        g.agregar_arista((i,j),(i,j-1),min(symbols[mapa[i][j]][1], symbols[mapa[i][j-1]][0]))
                        g.agregar_arista((i,j),(i+1,j),min(symbols[mapa[i][j]][1], symbols[mapa[i+1][j]][0]))
                        g.agregar_arista((i,j),(i-1,j),min(symbols[mapa[i][j]][1], symbols[mapa[i-1][j]][0]))

            #luego los limites laterales del mapa
            for i in range(1,x-1):
                #si el punto del mapa es un hielo, el flujo sale desde su nodo fantasma
                if mapa[i][0]== '.':
                    g.agregar_arista(((i,0),b),(i+1,0),1)
                    g.agregar_arista(((i,0),b),(i-1,0),1)
                else:
                    g.agregar_arista((i,0),(i+1,0),min(symbols[mapa[i][0]][1], symbols[mapa[i+1][0]][0]))
                    g.agregar_arista((i,0),(i-1,0),min(symbols[mapa[i][0]][1], symbols[mapa[i-1][0]][0]))

                #si el punto del mapa es un hielo, el flujo sale desde su nodo fantasma
                if mapa[i][y-1]== '.':
                    g.agregar_arista(((i,y-1),b),(i+1,y-1),1)
                    g.agregar_arista(((i,y-1),b),(i-1,y-1),1)
                else:
                    g.agregar_arista((i,y-1),(i+1,y-1),min(symbols[mapa[i][y-1]][1], symbols[mapa[i+1][y-1]][0]))
                    g.agregar_arista((i,y-1),(i-1,y-1),min(symbols[mapa[i][y-1]][1], symbols[mapa[i-1][y-1]][0]))
            
            #luego los limites superiores del mapa
            for j in range(1,y-1):
                if mapa[0][j]== '.':
                    g.agregar_arista(((0,j),b),(0,j+1),1)
                    g.agregar_arista(((0,j),b),(0,j-1),1)
                else:
                    g.agregar_arista((0,j),(0,j+1),min(symbols[mapa[0][j]][1], symbols[mapa[0][j+1]][0]))
                    g.agregar_arista((0,j),(0,j-1),min(symbols[mapa[0][j]][1], symbols[mapa[0][j-1]][0]))
                if mapa[x-1][j]== '.':
                    g.agregar_arista(((x-1,j),b),(x-1,j+1),1)
                    g.agregar_arista(((x-1,j),b),(x-1,j-1),1)
                else:
                    g.agregar_arista((x-1,j),(x-1,j+1),min(symbols[mapa[x-1][j]][1], symbols[mapa[x-1][j+1]][0]))
                    g.agregar_arista((x-1,j),(x-1,j-1),min(symbols[mapa[x-1][j]][1], symbols[mapa[x-1][j-1]][0]))
            
            if x >1:
                for j in range(y):
                    if mapa[0][j]== '.':
                        g.agregar_arista(((0,j),b),(1,j),1)
                    else:
                        g.agregar_arista((0,j),(1,j),min(symbols[mapa[0][j]][1], symbols[mapa[1][j]][0]) )
                    if mapa[x-1][j]== '.':
                        g.agregar_arista(((x-1,j),b),(x-2,j),1)
                    else:
                        g.agregar_arista((x-1,j),(x-2,j),min(symbols[mapa[x-1][j]][1], symbols[mapa[x-2][j]][0]) )
            
            if y >1:
                for i in range(x):
                    if mapa[i][0]== '.':
                        g.agregar_arista(((i,0),b),(i,1),1)
                    else:
                        g.agregar_arista((i,0),(i,1),min(symbols[mapa[i][0]][1], symbols[mapa[i][1]][0]) )
                    if mapa[i][y-1]== '.':
                        g.agregar_arista(((i,y-1),b),(i,1),1)
                    else:
                        g.agregar_arista((i,y-1),(i,y-2),min(symbols[mapa[i][y-1]][1], symbols[mapa[i][y-2]][0]) )

            max_flow = g.edmonds_karp((0,n+1), (n+1,n+1))
            
            print(max_flow)

            results.append(max_flow)
            b = input()
            x,y,p = map(int, input().split())

    except EOFError:
        pass
    for result in results:
         print(result)

if __name__ == "__main__":
    main()
