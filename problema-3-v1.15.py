def solution(tree,height,f,accorn):
    mem1 = [[0]*tree for _ in range(height)]
    for t in range(tree):
        mem1[0][t] = accorn[t][0]

    for h in range(1,height):
        if h-f >= 0:
            maxi = max(mem1[h-f])
        else:
            maxi = 0
        for t in range(tree):
            mem1[h][t] = max(mem1[h-1][t], maxi) + accorn[t][h]

    return max(mem1[height-1])

def main():
    c = int(input())
    for _ in range(c):
        t,h,f = map(int, input().split())
        accorn_map = [[0]*h for _ in range(t)]
        for tree in range(t):
            accorn_tree = list(map(int, input().split()))
            for a in accorn_tree[1:]:
                accorn_map[tree][a-1] += 1
        print(solution(t,h,f,accorn_map))

if __name__ == "__main__":
    main()