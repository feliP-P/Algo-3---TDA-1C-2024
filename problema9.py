def costos(n,aristas,nodos):
    for nodo in range(n):
        for destino in range(nodo,n):
            if nodo != destino:
                costo = 0
                for i in range(4):
                        c = abs(nodos[nodo][i] - nodos[destino][i])
                        if c > 5:
                            costo+= 10-c
                        else:
                            costo+=c
                aristas[nodo][destino] = costo
                aristas[destino][nodo] = costo

def min_arista1(nodos,aristas,visitados):
    min = (21,visitados[0])
    for nodo in visitados:
        for destino in range(len(nodos)):
            if destino not in visitados and aristas[nodo][destino] < min[0]:
                min = (aristas[nodo][destino],destino,nodo)
    return min

def prim(n,nodos,aristas):
    costo_aristas = 0
    visitados = [0]
    #arbol = []
    while len(visitados) < n:
         min = min_arista1(nodos,aristas,visitados)
         visitados.append(min[1])
         #arbol.append((min[2],min[1]))
         costo_aristas += min[0]

    return costo_aristas

def main():
    respuestas = []
    test_case = int(input())
    
    for _ in range(test_case):
        string_nodes = input().split()
        n = int(string_nodes[0])
        nodos = []
        

        #creamos nuestros nodos a partir de nuestro input str (separamos los digitos en listas de de 4 números)
        for i in range(n):
            nodos.append( [int(x) for x in string_nodes[i+1]] )
        
        


        aristas = [[0]*(n+1) for _ in range(n+1)]
        #calculamos el costo de todas las aristas entre los nodos (el costo de cambiar de una contraseña a otra)
        #O(n**2)/2
        costos(n,aristas,nodos)

        rolls = prim(n,nodos,aristas)

        #agregamos el nodo [0,0,0,0] y calculamos su distancia al resto de nodos
        nodos.append([0,0,0,0])
        
        #aristas_0 = [0 for _ in range(n)]
        aristas_0 = []
        for nodo in range(n):
            costo = 0
            for i in range(4):
                        c = nodos[nodo][i]
                        if c > 5:
                            costo+= 10-c
                        else:
                            costo+=c
            #aristas_0[nodo] = costo
            aristas_0.append(costo)
        #agregamos la conexión al nodo [0000] como la cantidad de rolls iniciales

        rolls += min(aristas_0)
        
        respuestas.append(rolls)

    for i in range(test_case):
        print(respuestas[i])

if __name__ == "__main__":
    main()
