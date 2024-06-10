def grafo(conections, switches, rooms):
    recorridos_posibles = [[]*11]
    for r in range(1,11):

        for n in range(len(switches[r])):
            if (r in switches[switches[r][n]]) and (switches[r][n] in conections[r]):
                recorridos_posibles[r].append(switches[r][n])

    distancia = [-1 for _ in range(11)]
    distancia[1] = 1
    for o in range(1,10):
        for f in range(len(recorridos_posibles[o])+1):
            if distancia[f] == -1:
                distancia[f] = distancia[o] + 1
    if distancia[rooms] == -1:
        print("The problem cannot be solved.")
    else:
        print(f"The problem can be solved in {distancia[rooms]} steps.")


def main():
    r, d, s = map(int, input().split())

    while r != 0:
        conections = []
        switches = [[]*(r+1)]
        #do a job
        for doors in d:
            conections.append(list(map(int, input().split())))
        for switch in s:
            origen, final = map(int, input().split())
            switches[origen].append(final)
        grafo(conections, switches, r)

        r, d, s = map(int, input().split())
